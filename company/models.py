from django.db import models

from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.

account_type_choices = (
    ('NC', 'NOT COMPANY'),
    ('TC', 'TRUCKING'),
    ('HH', 'HOME HEALTH'),
    ('AG', 'AGENCY')
)

# User = get_user_model()
USER = get_user_model()

class UserCompanyModel(models.Model):
    
    company_name = models.CharField(blank=True, null=True, max_length=200)
    dot_number = models.CharField(blank=True, null=True, max_length=30)
    account_type = models.CharField(max_length=5, choices=account_type_choices)
    add_date = models.DateField(auto_now_add=True)
    quest_client_id = models.CharField(blank=True,null=True, max_length=30)
    company_user = models.ForeignKey(USER, on_delete=models.CASCADE)
    consortium_purchased = models.BooleanField(default=False)
    is_company_true = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.company_name

    def rtnDot(self):
        if self.account_type == 'FMC':
            return "T"
        else:
            return "F"

    def is_company(self):
        return self.is_company_true

    def is_dot(self):
        if self.account_type == 'TC':
            return True
        else:
            return False
            
    
    class Meta:
        ordering = ['add_date']
        