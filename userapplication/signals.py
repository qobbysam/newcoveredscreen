from django.dispatch import Signal, receiver

from oscar.apps.order.signals import order_placed
user_registered = Signal()
user_logged_in = Signal()

create_purchase_consortium = Signal()
create_purchase_drugtest = Signal()
create_employee_signal = Signal()


def notifyconsortium(sender, user, detail):

    print("notifyconsortium")
    
    create_purchase_consortium.send_robust(sender=sender, user=user, detail=detail)

def notifydrugtest(sender, user, order):

    print("notifydrugtest")
    create_purchase_drugtest.send_robust(sender=sender, user=user, order=order)



def notifyemployee(sender, user, order):
    print("sending employee")

    create_employee_signal.send_robust(sender=sender, user=user, order=order)


@receiver(order_placed)
def order_placed_receiver(sender, user, order , **kwargs):
    print("receiver called")
    print(order)

    ##find order category

    lines = order.lines.all()

    product_ = lines[0]

    product_class = product_.product.get_product_class()

    print(product_class)


    print(product_class.id) 



    for line in lines:
        product_c = line.product.get_product_class()

        id_ = product_c.name
        notifyemployee(sender=sender, user=user, order=order.number)
        if id_ == 'Consortium_Membership_Class':

            detail = {}

            notifyconsortium(sender=sender,user=user,detail =detail )
        elif id_ == 'Drug_Test_Class':
            
            notifydrugtest(sender=sender, user=user, order=order.number)

            



def async_caller(user,order):
    from django_q.tasks import async_task, result
    from userapplication.tasks import employee_creator

    async_task(employee_creator, user,order)

    ##send category create signal






