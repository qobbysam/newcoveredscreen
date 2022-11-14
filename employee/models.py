
from django.db import models
from datetime import date

# Create your models here.
from company.models import UserCompanyModel

class EmployeeModel(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    middle_name = models.CharField(blank=True, null=True,max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    phone_number = models.CharField(blank=True, null=True, max_length=20)
    unique_id = models.CharField(blank=True, null=True, max_length=20)
    company = models.ForeignKey(UserCompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    add_date = models.DateField(auto_now_add=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_selected_random = models.BooleanField(default=False)
    is_drugtest_bought = models.BooleanField(default=False)
    is_dot_employee = models.BooleanField(default=False)

    def is_drug_test_bought(self):
        return self.is_drug_test_bought

    
    def isdotemployee(self):
        return self.is_dot_employee

    def is_random_selected(self):
        return self.is_random_selected
   
    def is_drug_test_bought(self):
        return self.is_drug_test_bought

    def isdotemployee(self):
       return self.is_dot_employee
 
    def locupdatecreated(self, empobj):
        self.first_name = empobj['first-name']
        self.last_name = empobj['last-name']
        self.middle_name = empobj['middle-name']
        try:
            self.date_of_birth = empobj['dob']
        except Exception as e:
            print(e)

        self.is_dot_employee = empobj['is-dot']
        self.is_active = True
        self.phone_number = empobj['phone-number']
        self.unique_id = empobj['primary-id']
        self.company = UserCompanyModel(id=empobj['company'])
        self.email = empobj['email']
        super().save()
        
    def locupdatefound(self, empobj):
        self.first_name = empobj['first-name']
        self.last_name = empobj['last-name']
        self.middle_name = empobj['middle-name']
        try:
            self.date_of_birth = empobj['dob']
        except Exception as e:
            print(e)
        self.phone_number = empobj['phone-number']
        self.unique_id = empobj['primary-id']
        super().save()
        

    def __str__(self):
        return "%s, %s "% (self.first_name , self.last_name)
    
    # def updatecreated(
    #                     self, 
    #                     first_name, 
    #                     last_name,
    #                     phone_number,
    #                     date_of_birth,
    #                     is_dot_employee ,
    #                     unique_id
    #                      ):

    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.phone_number = phone_number
    #     self.unique_id = unique_id      
    #     self.date_of_birth = date_of_birth
    #     self.is_dot_employee = is_dot_employee
    #     self.is_active = True
    #     self.add_date = date.today()

    #     super().save()


    # def updatefound(self, first_name, last_name, phone_number, date_of_birth, unique_id):

    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.phone_number = phone_number
    #     self.date_of_birth = date_of_birth
    #     self.unique_id = unique_id


    #     super().save()



    def toggleupdate(self):

        if self.is_active:
            self.is_active = False
        
        else:
            self.is_active = True

        super().save()
    
    def toggle_is_random_selected(self, value):

        self.is_random_selected = value

        super().save()

    def toggle_is_drug_test_bought(self, value):
        self.is_random_selected = value


    def is_random_selected(self):
        return self.is_random_selected
    
    def is_drug_test_bought(self):
        return self.is_drug_test_bought

    def isdotemployee(self):
        return self.is_dot_employee
    

    class Meta:
        ordering = ['add_date']

        unique_together = ('email', 'company')
