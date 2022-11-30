#from django.db.models import signals
from django.dispatch import receiver

from userapplication.orderhandler import create_purchase_drugtest

from drugtest.tasks import sendApiRequest, checkApiSuccess

from drugtest.models import QuestOrderModel, DrugTestModel
from django_q.tasks import async_task, result

@receiver(create_purchase_drugtest)
def create_purchse_drugtest(sender, user, order, **kwargs):
    print("calling create drugtest order pruchase")
    
    async_task(sendApiRequest,user=user,order=order, hook=checkApiSuccess )