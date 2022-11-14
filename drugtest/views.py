
from datetime import datetime
import json as je
import time
from urllib import request
import uuid
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from drugtest.models import DrugTestModel, QuestOrderModel
# Create your views here.


sample_locations = '''
        {
            "data": [
            {
                "pk": 1,
                "csl":"001",
                "detail": {
                    "sitename": "Lab Corp One",
                    "address1" : "555 cleveland avenue",
                    "address2": "",
                    "city": "columbus",
                    "state": "OH",
                }
            },
            {
                "pk": 2,
                "csl":"001",
                "detail": {
                    "sitename": "Lab Corp Two",
                    "address1" : "555 cleveland avenue",
                    "address2": "",
                    "city": "columbus",
                    "state": "OH",
                }
            },
            {
                "pk": 3,
                "csl":"001",
                "detail": {
                    "sitename": "Lab Corp Three",
                    "address1" : "555 cleveland avenue",
                    "address2": "",
                    "city": "columbus",
                    "state": "OH",
                }
            },
            ]
        }
'''


sample_data = [
    {"pk": 1, "csl":"001", "detail": {"sitename": "Lab Corp 1", "address1" : "555 cleveland avenue",
                    "address2": "",
                    "city": "columbus",
                    "state": "OH"} }
]


class DrugTestListView(TemplateView):

    template_name = 'drugtest/drug_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        user = self.request.user

        data = DrugTestModel.objects.filter(company= user.default_company).order_by('-order_details__date_added')

        print(data)
        print(user)

        #context['orderdata'] = data


        p = Paginator(data, 5)
        
        try:
            page_number = self.request.GET.get('page')

        
            page_obj = p.get_page(page_number)
        

            context['page_obj'] = page_obj
        except:
            context['page_obj'] = p.get_page(1)

        




        return context


class ViewOneDrugTest(DetailView):

    model= QuestOrderModel

    template_name = 'drugtest/drug_one.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cur_model = QuestOrderModel.objects.get(pk=self.object.id)

        get_respone =  self.get_reponse_obj(cur_model=cur_model)
        print(get_respone)
        print("ft")
        context['get_info'] = get_respone

        return context

    def get_response_detail(self, key):
        print("getting response detail")
        time.sleep(3)

        #url = settings.QUEST_URL + 'sendend/'

        url = settings.QUEST_URL + 'getkey/'

        params = {}

        params['key'] = key

        r = requests.get(url, params=params)

        data = r.json()
        #print (data)

        return data

    def get_response_api(self, cur_model):

                print("sending response")
                url = settings.QUEST_URL + 'sendend/'

                info_dic = {}

                info_dic['last_get_info'] = datetime.now()
                info_dic ['get_info_key'] = uuid.uuid4().hex


                params = {}
                params['clientid'] = info_dic['get_info_key']
                
                params['sendtype'] = "getorderdetails"

                json_body = {}

                json_body['questOrderId'] = cur_model.quest_id
                json_body['referenceTestId'] = cur_model.quest_reference_id

                #js = je.dumps(json_body)
                r = requests.post(url=url, params=params, json=json_body)

                #print(js)
                print(params)

                print(r.status_code)

                if r.status_code == 200:

                    json_l = self.get_response_detail(info_dic['get_info_key'])
                    #print(json)
                    
                    
                    res = self.handle_get_info(json_l, info_dic ,True)

                    info_dic = res['info_dic']

                    cur_model.update_get_info(info_dic)

                    return res['out_obj']

                else:
                    res = self.handle_get_info(None,info_dic, False)

                    info_dic = res['info_dic']

                    cur_model.update_get_info(info_dic)
                    
                    return res['out_obj']



    def get_reponse_obj(self, cur_model):


        #print(cur_model)



        if cur_model.get_info_pass is not None and  cur_model.get_info_pass and False:
            now = datetime.now()

            last = cur_model.last_get_info
            
            diff = last - now

            min  = diff.total_seconds()/60

            if min < 2880:

                res = self.handle_get_info(cur_model.get_info_json, None, True)

                return res['out_obj']
            else:
                res = self.get_response_api(cur_model)

                return res

                
        else:
            res = self.get_response_api(cur_model)
            return res


            
    def handle_get_info(self, json_obj, info_dic,passresult):

        if not passresult:

            info_dic['get_info_pass'] = False
            info_dic['get_info_error_message'] = json_obj
            info_dic['get_info_json'] = "{}"
            res_loc = self.parse_json(json_obj, passresult)
            res_loc['pass'] = False

            res = {}
            res['info_dic'] = info_dic
            res['out_obj'] = res_loc
            return res
        else:

            info_dic['get_info_pass'] = True
            info_dic['get_info_error_message'] = "{}"
            info_dic['get_info_json'] = json_obj
            res_loc = self.parse_json(json_obj, passresult)

            res_loc['pass'] = True

            res = {}
            res['info_dic'] = info_dic
            res['out_obj'] = res_loc
            return res

    def parse_json(self, json_obj, passresult):

        out_res = {}

        #print (json_obj)
        
        
        #obj = je.loads(json_obj)







        if not passresult:
            pass

        else:
            out_res['pass'] = True

            print(json_obj)
            obj = json_obj[0]




            print(obj)
            first = obj[0]
            res  = first['result']

            obj_res =    je.loads(res)

            out_res['display_url'] = obj_res['QuestMethodResponse']['DisplayURL']

            print(out_res)


        return out_res

'''
{
    'client_id': '268e13a67a404127bd48aafee5bcde42',
     'result': '{
        "QuestMethodResponse": {
            "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema", 
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
            "MethodID": "GETORDERDETAIL", 
            "ClientReferenceID": "p8g61ZemdWqC", 
            "ReferenceTestID": "Q00189114", 
            "QuestOrderID": "15008085", 
            "ResponseStatusID": "SUCCESS", 
            "DisplayURL": "https://esp-load.employersolutions.com/Integration/OrderDetail?access_token=3796e9fd-97c7-4f0a-a86c-81770b80599b", 
            "Errors": null
            }}', 
            'table': 'getorderdetails', 'time_added': '2022-08-30 12:17:39.224332', 'updated': False}
'''




    



def searchApiView(request):

    if request.method == 'POST':
        # zip_code = request.query_params.get('zipcode', None) 
        # city = request.query_params.get('city', None)
        # range = request.query_params.get('range', None)

        #return JsonResponse(sample_locations, safe=False)

        body_unicode = request.body.decode('utf-8')
        body = je.loads(body_unicode)

        params = {}
        url = settings.QUEST_URL + "locations/"
        r = requests.post(url, json=body)

        if r.status_code == 200:


            return JsonResponse(r.json(), safe = True)
        else:
            return JsonResponse({"msg": "could not get the values"})

