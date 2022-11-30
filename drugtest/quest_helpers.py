import uuid
from datetime import datetime
import requests
from django.conf import settings

from oscar.apps.order.models import Order


from .models import DrugTestModel, QuestOrderModel
from .const import DRUG_TEST_PRODUCT
from company.models import UserCompanyModel

def get_is_dot(company):

    if company.is_dot():
        return 'T'
    else:
        return 'F'

def drugtestvalues(linesvalues):
    out = {}

    for val in linesvalues:
        
            out[val[-2]] = val[-1] 
    
    return out

def buildorder(user, company, details):

    order_dot = {}

    

    order_body = {}

    order_body['emails'] = [details['email']]
    
    if user.email == details['email']:
        pass
    else:
        order_body['emails'] += [user.email]

    if details['middle-name'] == "none":

        order_body['middleName'] = ""

    else:
        order_body['middleName'] = details['middle-name']

    order_body['unitcodes'] = ["65105N", "11070N"]
    order_body['firstName'] = details['first-name']
    order_body['lastName'] = details['last-name']

   
    order_body['primaryID'] = details['license-number']
    order_body['dob'] = details['date-of-birth']
    order_body['primaryPhone'] = details['phone-number']
    order_body['secondaryPhone'] = "" 
    order_body['contactName'] = user.get_full_name()
    order_body['telephoneNumber'] = user.phone
    order_body['labAccount'] = settings.QUEST_ACCOUNT_NUMBER
    
    order_body['collectionId'] = details['collection-location']
    order_body['csl'] = settings.QUEST_CSL

    order_body['clientReferenceID'] = company.quest_client_id
    
    if details['is-dot'] == 'T' :


        order_body['dotTest'] = details['is-dot']
        order_body['testingAuthority'] = company.dot_number
    else:
        order_body['dotTest'] = details['is-dot']
        order_body['testingAuthority'] = ""

    order_body['reasonForTestID'] = details['test-reason']
    order_body['observedRequested'] = details['observe-requested']
    order_body['splitSpecimenRequested'] = details['split-specimen-requested'] 

    order_dot['orderBody'] = order_body

    return order_dot




class QuestFirst:

    def __init__(self,order,user,) -> None:
        self.order = order
        self.user = user
        self.company = UserCompanyModel.objects.get(pk=int(user.default_company_key))


    def firstSave(self, body) -> QuestOrderModel:
        to_call_key = uuid.uuid4().hex

        to_save = QuestOrderModel.objects.create(
            stage="CT",
            client_id = body['orderBody']['clientReferenceID'],
            last_call_key  = to_call_key,
            date_added = datetime.now(),
            from_order = self.order
        )

        to_save.save()

        to_save_drug_test = DrugTestModel.objects.create(order_details = QuestOrderModel(id=to_save.id), company=UserCompanyModel(id=self.company.pk))

        to_save_drug_test.save()

        return to_save


    def firstSend(self, body):

        to_save = self.firstSave(body)
        
        params = {}

        params['clientid'] = to_save.last_call_key
        params['sendtype'] = 'createorderbuild'
        data = body
        print ("sending")

        print(body)

        url = settings.QUEST_URL + "sendend/"
        r = requests.post(url, params=params,json=data)
        print("request sent")
        if r.status_code == 200:

            to_save.updateStage("AC")
            return to_save.last_call_key
        else:
            to_save.updateStage("ST")
            return to_save.last_call_key


    def sendOrders(self, to_send):

        keys = []
        for detail in to_send:
            body = buildorder(self.user, self.company, detail)

            key = self.firstSend(body)

            keys.append(key)

        return keys



    def getOrderInfo(self):

        order_info = Order.objects.get(number=self.order)

        out_info = []

        for line in order_info.lines.all():

            print(line.product.product_class, " c ", DRUG_TEST_PRODUCT )
            c = line.product.product_class
            if str(c)== DRUG_TEST_PRODUCT:

                attr = line.attributes.all()
                
                attr_v = attr.values_list()

                print(attr_v)
                vals = drugtestvalues(attr_v)

                vals['is-dot'] = get_is_dot(self.company)

                out_info.append(vals)


        return out_info


    def handleFirst(self):

        to_send = self.getOrderInfo()

        keys = self.sendOrders(to_send)

        self.keys = keys
        self.to_send = to_send



class QuestSecond:

    def __init__(self, questfirst) -> None:
        self.questfirst = questfirst
        self.pass_keys = []
        self.failed_keys = []

    def handleSecond(self):
        for key in self.questfirst.keys:
            self.updateResponse(key)
    

    def updateResponse(self, key):
        url = settings.QUEST_URL + 'getkey/'

        params = {}

        params['key'] = key

        r = requests.get(url, params=params)



        if r.status_code == 200:

            data = r.json()

            if len(data) != 0:
                first = data[0]

                self.updateResponseDB(first,key,True)
            else:
                self.updateResponseDB(None, key, False)
        else:
            data = r.json()
            self.updateResponseDB(data['msg'],key,False)


    def updateResponseDB(self, response, key,success):
        q_order = QuestOrderModel.objects.get(last_call_key=key)

        if response is None:
            response = 'bad api response'

        if success:
            q_order.updateResponse(response)
            self.pass_keys.append(key)
        else:
            q_order.badResponse(response)
            self.failed_keys.append(key)


class QuestThird:

    def __init__(self,questsecond) -> None:
        
        self.questsecond = questsecond

    def finalrun(self):
        self.resolvepass()
        self.resolvefail() 

    def resolvepass(self):

        for key in self.questsecond.pass_keys:

            drug_obj = QuestOrderModel.objects.get(last_call_key = key)

            drug_obj.updateStage('SU')

    def resolvefail(self):
        
        for key in self.questsecond.failed_keys:

            drug_obj = QuestOrderModel.objects.get(last_call_key = key)

            drug_obj.updateStage('AE')
    
