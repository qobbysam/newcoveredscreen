
from oscar.apps.order.models import Order
from company.models import UserCompanyModel
from employee.models import EmployeeModel


def employee_creator(user, order):
    
    user_company = UserCompanyModel.objects.get(pk=user.default_company)

    if not user_company.is_company():

        pass
    else:

        #order_info = Order.objects.get(number=order)


        employee_orders = get_info(user, order)

        for employee in employee_orders:
            print(employee)
            newemployee, created = EmployeeModel.objects.get_or_create(email=employee['email'], company=UserCompanyModel(id=employee['company']))

            if created:

                newemployee.locupdatecreated(employee)

            else:
                newemployee.locupdatefound(employee)


def get_info(user,order):

    out = []

    order_info = Order.objects.get(number=order)
    for line in order_info.lines.all():
        cats = line.product.get_categories().all()

        
        for cat in cats:

            if cat.name == 'employee':


                one_info = {}
                val_l= line.attributes.all()
                val_list = val_l.values_list()

                one_info['company'] = user.default_company
                one_info['is-dot'] = UserCompanyModel.objects.get(id=user.default_company).is_dot()

                values = get_values(one_info, val_list)
                out.append(values)
        
    return out


def get_values(obj, val_list):
    
    print(val_list)
    for v in val_list:
        end = v[-1]
        end_b_one = v[-2]

        if end_b_one == 'dob':
            obj['dob'] = end
        
        elif end_b_one == 'email':
            obj['email'] = end
        elif end_b_one  == 'phone-number':
            obj['phone-number'] = end

        elif end_b_one == 'first-name':
            obj['first-name'] = end
        
        elif end_b_one == 'last-name':
            obj['last-name'] = end
        
        elif end_b_one == 'middle-name':
            obj['middle-name'] = end
        
        elif end_b_one == 'primary-id':
            obj['primary-id'] = end
    
    return obj
    
