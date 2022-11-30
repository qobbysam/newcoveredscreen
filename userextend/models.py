from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.apps import apps

from userextend.managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects =  models.Manager()
    

    spouse_name = models.CharField(blank=True, max_length=100)

    phone = models.CharField(verbose_name='phone',blank=True, null=True, max_length=30)
    profile_pic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    default_company_name = models.CharField(max_length=200, blank=True, null=True)
    default_company_key = models.CharField(max_length=200, blank=True, null=True)
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    
    def get_summary(self):
        out = {}
        out['email'] = self.email 
        out['phone'] = self.phone
        out['first_name'] = self.first_name
        out['last_name'] = self.last_name

        out['company'] = self.get_company_summary()

        return out
    
    def get_company_summary(self):
     #from company.models import UserCompanyModel
   
        company_model = apps.get_model('company', 'UserCompanyModel')
        company = company_model.objects.get(id=self.default_company_key)

        company_summary = company.get_summary()

        return company_summary
    
    def is_company(self, account_type) -> bool:

        company_model = apps.get_model('company', 'UserCompanyModel')
        company = company_model.objects.get(id=self.default_company_key)

        #return company.is_company()

        return self.account_type != 'NC'