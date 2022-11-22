
from django.dispatch import Signal, receiver

from oscar.apps.order.signals import order_placed
user_registered = Signal()
user_logged_in = Signal()

create_purchase_consortium = Signal()
create_purchase_drugtest = Signal()
create_employee_signal = Signal()




class OrderHandler:

    def __init__(self, order, user, sender) -> None:
        self.order = order
        self.user = user 
        self.sender = sender

    

    def notifyconsortium(self,sender, user, detail):

        print("notifyconsortium")
        
        create_purchase_consortium.send_robust(sender=sender, user=user, detail=detail)

    def notifydrugtest(self,sender, user, order):

        print("notifydrugtest")
        create_purchase_drugtest.send_robust(sender=sender, user=user, order=order)



    def notifyemployee(self,sender, user, order):
        print("sending employee")

        create_employee_signal.send_robust(sender=sender, user=user, order=order)


    def handle(self, sender):
        lines = self.order.lines.all()

        for line in lines:
            product_c = line.product.get_product_class()

            id_ = product_c.name
            self.notifyemployee(sender=sender, user=self.user, order=self.order.number)
            if id_ == 'Consortium_Membership_Class':

                detail = {}

                self.notifyconsortium(sender=sender,user=self.user,detail =detail )
            elif id_ == 'Drug_Test_Class':
                
                self.notifydrugtest(sender=sender, user=self.user, order=self.order.number)
