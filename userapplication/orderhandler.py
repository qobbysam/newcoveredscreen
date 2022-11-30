
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
        
        create_purchase_consortium.send_robust(sender=sender, user=user, type_consortium=detail)

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

                detail = self.get_consortium_type(line)

                self.notifyconsortium(sender=sender,user=self.user,detail =detail )
            elif id_ == 'Drug_Test_Class':
                
                self.notifydrugtest(sender=sender, user=self.user, order=self.order.number)

    def get_consortium_type(self, line):
        lines_attr = line.attributes.all()

        val_list = lines_attr.values_list()
        
        out_val = ""
        for v in val_list:
            end = v[-1]
            end_b_one = v[-2]

            if end_b_one == 'empty-one':
                if end == "Basic":
                    out_val = 'bs'
                elif end == "Silver":
                    out_val = 'sl'
                elif end == 'Gold':
                    out_val = 'gd'
        return out_val
