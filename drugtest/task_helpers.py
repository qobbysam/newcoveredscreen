from datetime import datetime
import uuid
import requests
from django.conf import settings
from oscar.apps.order.models import Order
from .models import DrugTestModel, QuestOrderModel
from .const import DRUG_TEST_PRODUCT
from company.models import UserCompanyModel
import time
def drugtestvalues(linesvalues):
    out = {}

    for val in linesvalues:
        
            out[val[-2]] = val[-1] 
    
    return out


def getOrderInfo(order,company):

    print(dir(order))

    print(order, "here")

    order_info = Order.objects.get(number=order)

    out_info = []

    #clean_ = {}


    for line in order_info.lines.all():

        print(line.product.product_class, " c ", DRUG_TEST_PRODUCT )
        c = line.product.product_class
        if str(c)== DRUG_TEST_PRODUCT:

            attr = line.attributes.all()
            
            attr_v = attr.values_list()

            print(attr_v)
            vals = drugtestvalues(attr_v)

            vals['is-dot'] = get_is_dot(company)

            out_info.append(vals)


    return out_info



def get_is_dot(company):

    if company.is_dot():
        return 'T'
    else:
        return 'F'


def sendOrderRequest(user, company,order_info):
    print("sending order request")

    keys = []
    for detail in order_info:
        body = buildorder(user, company, detail)

        key = apicall(body,company)
        keys.append(key)

        updateCompanyEmployee(company, body)

    return keys



def updateCompanyEmployee(company, body):
    pass  

def apicall(body, company):
    to_call_key = uuid.uuid4().hex
    to_save = QuestOrderModel.objects.create(
        stage="CT",
        client_id = body['orderBody']['clientReferenceID'],
        last_call_key  = to_call_key,
        date_added = datetime.now()
    )

    to_save.save()

    to_save_drug_test = DrugTestModel.objects.create(order_details = QuestOrderModel(id=to_save.id), company=UserCompanyModel(id=company.pk))

    to_save_drug_test.save()

    params = {}

    params['clientid'] = to_call_key
    params['sendtype'] = 'createorderbuild'

    data = body

    print ("sending")

    print(body)
    url = settings.QUEST_URL + "sendend/"
    r = requests.post(url, params=params,json=data)
    print("request sent")
    if r.status_code == 200:

        to_save.updateStage("AC")
        return to_call_key
    else:
        to_save.updateStage("ST")
        return to_call_key

        #retry heres

        #if retries fail report an error


def updateResponse(user, key):


    #time.sleep(5)

    url = settings.QUEST_URL + 'getkey/'

    params = {}

    params['key'] = key

    r = requests.get(url, params=params)

    data = r.json()

    print(data)
    #print(dir(data))

    if len(data) != 0:
        first = data[0]

        updateresponseDB(first, key, True)
    else:

        updateresponseDB(None, key, False)

    



def updateresponseDB(response, key,success):

    if success:
        q_order = QuestOrderModel.objects.get(last_call_key=key)

        #response_obj = json.loads(response)

        print(dir(response))

        print(response)

        q_order.updateResponse(response)
    else:
        q_order = QuestOrderModel.objects.get(last_call_key=key)

        q_order.badResponse("not successful")





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



