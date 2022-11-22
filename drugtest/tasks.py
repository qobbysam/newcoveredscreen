
from django_q.tasks import async_task, result
from drugtest.quest_helpers import QuestFirst, QuestSecond, QuestThird

def sendApiRequest(user,order):

    questfirst = QuestFirst(order,user)

    questfirst.handleFirst()
    #keys =  sendOrderRequest(user,company,order_info)
    return questfirst


def checkApiSuccess(task):
    print('checking api response')

    if task.success:

        questfirst = task.result

        async_task('drugtest.tasks.waitForResponse', questfirst, hook='drugtest.tasks.successResponseCheck')

    else:
        print("resending task")



def waitForResponse(questfirst):

    print('waiting for quest response')

    questsecond = QuestSecond(questfirst)

    questsecond.handleSecond()

    return questsecond



def successResponseCheck(task):

    if task.success:

        questsecond= task.result

        async_task('drugtest.tasks.sendSuccessTask', questsecond, hook='drugtest.tasks.checkSendResponseSuccess')


def sendSuccessTask(questsecond):

    print('sending success task')

    questthird = QuestThird(questsecond)

    questthird.finalrun()

    return questthird

    



def checkSendResponseSuccess(task):

    if task.success:
        print("completed all processes for drugtest creation")