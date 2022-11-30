from datetime import datetime, timedelta
from django.db import models

from company.models import UserCompanyModel
# Create your models here.

consortim_choices = (('bs', 'bronze'), ("sl", "silver"),('gd', "gold"))

class ConsortiumModel(models.Model):

    company_name = models.CharField(null=True, blank=True, max_length=200)
    start_date = models.DateField(null=True, blank=True, auto_now_add=True)
    end_date = models.DateField(null=True, blank=True,)
    active = models.BooleanField(default=False)

    
    company = models.ForeignKey(UserCompanyModel, on_delete=models.CASCADE)

    consortium_type = models.CharField(choices=consortim_choices, default="bs", blank=True, null=True, max_length=3)

    def __str__(self):
        return self.company_name

    def updatecreated(self,start_date, end_date, active, company_name):

        self.active = active
        self.start_date = start_date
        self.end_date = end_date
        self.company_name = company_name

        super().save()

    def upgrade_consortium(self, upgrade_to):
        self.consortium_type = upgrade_to
        super().save()
    
    def generate_ms(self):

        ms = {}

        ms['active'] = self.active
        ms['company_name'] = self.company_name
        ms['start_date'] = self.start_date.strftime("%b %d, %Y")
        ms['end_date'] = self.end_date.strftime("%b %d, %Y")
        ms['can_purchase'] = self.can_purchase()
        ms['is_expired'] = self.is_expired()
        ms['consortium_type'] = self.consortium_type
        return ms
    
    def can_purchase(self):

        # end_date = self.end_date
        # current_date = datetime.today()

        # if end_date == '':
        #     return False

        # d1 = end_date.strptime("%Y/%m/%d")
        # d2 =  current_date.strptime("%Y/%m/%d")

        # delta = d1-d2



        # if delta < 60:
            
        #     return True
        # else:
        #     print("second stage")
        #     return False
        return True
        
    def is_expired(self):
        # end_date = self.end_date
        # current_date = datetime.today()

        # d1 = end_date.strptime(end_date, "%Y/%m/%d")
        # d2 = current_date.strptime(current_date, "%Y/%m/%d")

        # delta = d1-d2

        # if delta < 0:
        #     return True
        # else:
        #     return False

        return False

class ConsortiumPurchaseCreation(models.Model):

    time_action = models.DateTimeField(auto_now_add=True)
    consortium = models.ForeignKey(ConsortiumModel,null=True, blank=True, on_delete=models.CASCADE)