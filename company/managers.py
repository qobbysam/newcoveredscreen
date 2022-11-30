from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# class CompanyManager(models.Manager):

#     def rtnDot(self):
#         if self.account_type == 'FMC':
#             return "T"
#         else:
#             return "F"

#     def is_company(self):
#         return self.is_company_true

#     def is_dot(self):
#         if self.account_type == 'TC':
#             return True
#         else:
#             return False
#     def get_summary(self):

#         if self.consortium_purchased:

#             out = self.get_consortium_summary()

#             out['consortium_purchased'] = self.consortium_purchased

#             return out
#         else:
#             out = {}   
#             out['consortium_purchased']  = self.consortium_purchased 

#             return out  
#     def get_consortium_summary(self):

#         consortium = ConsortiumModel.objects.get(id=self.id)

#         msg = consortium.generate_ms()

#         return msg