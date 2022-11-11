
from signal import signal
from django.db import models
from django.utils.crypto import get_random_string
#from django.db.models import signals
from django.dispatch import receiver
from django.dispatch import Signal

from userextend import signals
from userextend.models import CustomUser

from .models import UserCompanyModel

# @receiver(signals.user_registered_company, sender=Product) 
# def create_product(sender, instance, created, **kwargs):
#     print("Save method is called")


#User = get_user_model()

@receiver(signals.user_registered_company)
def create_company(sender, user, company , **kwargs):
    print("receiver called")
    print(company)

    val = UserCompanyModel.objects.create(
        company_name = company['company_name'],
        dot_number = company['dot_number'],
        account_type = company['account_type'],
        company_user = user,
        is_company_true = company['is_company'],
        quest_client_id = get_random_string(12),
        consortium_purchased = False

    )
    
    val.save()

    user_ = CustomUser.objects.get(pk=user.id)

    user_.default_company_key = val.id
    user_.default_company_name = val.company_name

    user_.save()


    #update profie default company

# signals.user_registered_company.connect(create_company) 
