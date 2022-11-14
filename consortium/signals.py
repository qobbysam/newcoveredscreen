




from signal import signal
from django.db import models
#from django.db.models import signals
from django.dispatch import receiver
from django.dispatch import Signal
from dateutil.relativedelta import relativedelta

from userapplication import signals
from userprofile.models import User
from company.models import UserCompanyModel

from .models import ConsortiumModel, ConsortiumPurchaseCreation


# @receiver(signals.user_registered_company, sender=Product) 
# def create_product(sender, instance, created, **kwargs):
#     print("Save method is called")


#User = get_user_model()
from datetime import date

@receiver(signals.create_purchase_consortium)
def create_purchase_consortium(sender, user, detail , **kwargs):
    print("create purchase receiver called")
    print(user)

    user_ = User.objects.get(pk=user.id)

    print("pass user")
    today = date.today()
    company_ = UserCompanyModel.objects.get(pk=user_.default_company)
    print("pass company")

    
    obj, created = ConsortiumModel.objects.get_or_create(company=company_)

    if created:
        obj.updatecreated(
            start_date = today,
            end_date = date(today.year + 1, today.month, today.day),
            active = True,
            company_name =  company_.company_name,


        )

        print("new consortium created")
    else:
        new_end = obj.end_date + relativedelta(years=1)
        obj.updatecreated(
        start_date = obj.end_date,
        end_date = new_end,
        active = True,
        company_name =  company_.company_name,)
            
        print ("consortim already exists")




    # new_consortim = ConsortiumModel.objects.create(
    #     company = company_,
        
    # )


    

    # new_consortim.end_date = 
    
    # #new_consortim.name = company_.company_name
    # new_consortim.active = True
    # new_consortim.start_date = today

    #new_consortim.save()
    # val = UserCompanyModel.objects.create(
    #     company_name = company['company_name'],
    #     dot_number = company['dot_number'],
    #     account_type = company['account_type'],
    #     company_user = user

    # )
    
    # val.save()

    # user_ = User.objects.get(pk=user.id)

    # user_.default_company = val.id

    # user_.save()


    #update profie default company

# signals.user_registered_company.connect(create_company) 
