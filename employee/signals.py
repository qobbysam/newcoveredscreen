from django.dispatch import receiver
from django.dispatch import Signal


from userapplication.signals import  async_caller
from userapplication.orderhandler import create_employee_signal
@receiver(create_employee_signal)
def handle_create_employee(sender, user, order, **kwargs):

    print('sending async task')
    async_caller(user,order)



    #async_task('employee.tasks.handleEmployee', user, order)
