
from django_q.tasks import async_task, result
from drugtest.models import DrugTestModel
from drugtest.task_helpers import getOrderInfo, sendOrderRequest, updateResponse
from company.models import UserCompanyModel

def sendApiRequest(user,order):
    company = UserCompanyModel.objects.get(pk=int(user.default_company_key))

    print('sending api request')
    order_info = getOrderInfo(order, company)

    print (order_info)


    keys =  sendOrderRequest(user,company,order_info)

    return user , keys

        


def checkApiSuccess(task):
    print('checking api response')

    if task.success:

        user,keys = task.result

        async_task('drugtest.tasks.waitForResponse', user, keys, hook='drugtest.tasks.successResponseCheck')

    else:
        print("resending task")



def waitForResponse(user, keys):

    print('waiting for quest response')

    for key in keys:
        updateResponse(user=user, key=key)
        

    return user, keys


def successResponseCheck(task):

    if task.success:

        user, keys = task.result

        async_task('drugtest.tasks.sendSuccessTask', user, hook='drugtest.tasks.checkSendResponseSuccess')

def sendSuccessTask(user,keys):

    print('sending success task')

    for key in keys:

        drug_obj = DrugTestModel.objects.get(get_info_key = key)

        drug_obj.updateStage('SU')
    

    



def checkSendResponseSuccess(task):

    if task.success:
        print("completed all processes for drugtest creation")