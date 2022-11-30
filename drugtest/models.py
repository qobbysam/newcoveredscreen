import json
from django.db import models

from company.models import UserCompanyModel
# Create your models here.

STAGE_CHOICES = (
    ('CT', 'CREATED'),
    ('ST', 'STARTED'),
    ('AC', 'API CALL SENT'),
    ('AR', 'API CALL RESPONSE'),
    ('AE', 'API CALL BAD'),
    ('SU', 'ALL STATUS SENT'),
    ('RR', 'RESULTS READY')

)

'''

{
    'client_id': '49b956be49234a50b484c7627c6b9471', 
    'result': '{
        "QuestMethodResponse": {
            "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema", 
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
            "MethodID": "CREATEORDER", 
            "ClientReferenceID": "p8g61ZemdWqC",
            "ReferenceTestID": "Q00188039",
            "QuestOrderID": "15006924", 
            "ResponseStatusID": "SUCCESS", 
            "Errors": null
                }
            }',
     'table': 'createorderbuild', 
     'time_added': '2022-08-26 05:05:00.736704', 
     'updated': False
     }
'''
class QuestOrderModel(models.Model):
    quest_id = models.CharField(max_length=30, blank=True, null=True)
    quest_reference_id = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=30, blank=True, null=True)
    extra  = models.CharField(max_length=300,blank=True, null=True)
    date_added = models.DateTimeField(auto_created=True, blank=True, null=True)
    stage = models.CharField(max_length=3, choices= STAGE_CHOICES, blank=True, null=True)
    last_call_key = models.CharField(max_length=255,blank=True, null= True)
    get_info_key = models.CharField(max_length=255,blank=True, null= True)
    last_get_info = models.DateTimeField(auto_created=True, blank=True, null=True)
    get_info_json = models.JSONField(blank=True, null=True)
    get_info_error_message = models.JSONField(blank=True, null=True)
    get_info_pass = models.BooleanField(default=False)
    step_complete = models.BooleanField(default=False)
    error_occured = models.BooleanField(default=False)
    error_message = models.CharField(max_length=255, blank=True, null=True)
    from_order = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return "{} {}", self.client_id, self.stage

    
    def updateStage(self, stage):
        self.stage = stage

        super().save()

    def updateResponse(self, response):

        result = response[0]

        #to_update = json.loads(result)

        result__ = result['result']

        result = json.loads(result__)

        result_1 = result['QuestMethodResponse']

        response_status = result_1['ResponseStatusID']


        if response_status == 'FAILURE':

            self.handle_failure(result_1)
        else:
            self.handle_success(result_1)

        print(response)
        print(dir(result))
        print(result)

    def update_get_info(self, info_dic):
        self.get_info_key = info_dic['get_info_key']
        self.get_info_json = info_dic['get_info_json']
        self.get_info_error_message = info_dic['get_info_error_message']
        self.last_get_info = info_dic['last_get_info']
        self.get_info_pass = info_dic['get_info_pass']
        
        super().save()

    def handle_failure(self, result):
        errors = result['Errors']

        self.updateStage('AE')

        
    def handle_success(self, result):

        quest_id = result['QuestOrderID']
        reference_id = result['ReferenceTestID']

        self.quest_id = quest_id
        self.quest_reference_id = reference_id

        super().save()

        self.updateStage('AR')

    def badResponse(self, message):
        self.error_occured = True
        self.error_message = message
        
        super().save()

        self.updateStage('AE')

    def __str__(self):

        return "%s" % (self.id)
'''
{'QuestMethodResponse':

        {
            '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema',

            '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 
            
            'MethodID': 'CREATEORDER', 
            
            'ClientReferenceID': '8wmRDgB8cqbU', 
            'ReferenceTestID': None, 
            'QuestOrderID': None, 
            'ResponseStatusID': 'FAILURE', 
            
            'Errors': {
                'Error': {
                    'ErrorID': '200', 
                    'ErrorDetail': 'Invalid Testing Authority.'
                    }
                }
            }
}
'''


'''
{
    'Qu__str__ returned non-string (type tuple)
 'ReferenceTestID': 'Q00188937', 
        'QuestOrderID': '15007887', 
        'ResponseStatusID': 'SUCCESS', 
        'Errors': None
        }
}

'''
        # self.quest_id = result['QuestOrderID']
        # self.quest_reference_id = result['ReferenceTestID']

        # extra = [result['ResponseStatusID'], result['MethodID']]

        # self.extra = ''.join(map(str, extra))

        












class DrugTestModel(models.Model):
    company = models.ForeignKey(UserCompanyModel, blank=True, null=True, on_delete=models.SET_NULL)
    order_details = models.ForeignKey(QuestOrderModel, blank=True, null=True, on_delete= models.SET_NULL)
    from_order = models.CharField(max_length=255, blank=True, null=True)







class DrugTestOrderFail(models.Model):
    user_company = models.ForeignKey(UserCompanyModel, blank=True, null=True, on_delete=models.SET_NULL)
    order_info = models.ForeignKey(QuestOrderModel, blank=True, null=True, on_delete=models.SET_NULL)



    def __str__(self):
            return self.user_company