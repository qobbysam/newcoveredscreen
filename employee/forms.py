from django import forms
from employee.models import EmployeeModel
from company.models import UserCompanyModel
state_choices = [
    ('OH', 'OHIO'),
    ('AL','Alabama'),
        ('AK','Alaska'),
        ('AS','American Samoa'),
        ('AZ','Arizona'),
        ('AR','Arkansas'),
        ('CA','California'),
        ('CO','Colorado'),
        ('CT','Connecticut'),
        ('DE','Delaware'),
        ('DC','District of Columbia'),
        ('FL','Florida'),
        ('GA','Georgia'),
        ('GU','Guam'),
        ('HI','Hawaii'),
        ('ID','Idaho'),
        ('IL','Illinois'),
        ('IN','Indiana'),
        ('IA','Iowa'),
        ('KS','Kansas'),
        ('KY','Kentucky'),
        ('LA','Louisiana'),
        ('ME','Maine'),
        ('MD','Maryland'),
        ('MA','Massachusetts'),
        ('MI','Michigan'),
        ('MN','Minnesota'),
        ('MS','Mississippi'),
        ('MO','Missouri'),
        ('MT','Montana'),
        ('NE','Nebraska'),
        ('NV','Nevada'),
        ('NH','New Hampshire'),
        ('NJ','New Jersey'),
        ('NM','New Mexico'),
        ('NY','New York'),
        ('NC','North Carolina'),
        ('ND','North Dakota'),
        ('MP','Northern Mariana Islands'),
        ('OH','Ohio'),
        ('OK','Oklahoma'),
        ('OR','Oregon'),
        ('PA','Pennsylvania'),
        ('PR','Puerto Rico'),
        ('RI','Rhode Island'),
        ('SC','South Carolina'),
        ('SD','South Dakota'),
        ('TN','Tennessee'),
        ('TX','Texas'),
        ('UT','Utah'),
        ('VT','Vermont'),
        ('VI','Virgin Islands'),
        ('VA','Virginia'),
        ('WA','Washington'),
        ('WV','West Virginia'),
        ('WI','Wisconsin'),
        ('WY','Wyoming')            

]

class EditEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeModel
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'unique_id', 'is_active']


class AddEmployeeForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    license_state = forms.ChoiceField(choices=state_choices)
    license_number = forms.CharField()
    phone_number = forms.CharField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()


    def save(self, user):
        print('saving employee')
        user_company = UserCompanyModel.objects.get(pk= user.default_company)


        new_emp, created = EmployeeModel.objects.get_or_create(
                            first_name = self.cleaned_data['first_name'],
                             last_name   = self.cleaned_data['last_name'],
                             email = self.cleaned_data['email'],
                             phone_number = self.cleaned_data['phone_number'],
                            company = user_company,
                            date_of_birth = self.cleaned_data['date_of_birth']



        )

        if created:
            print("new employee created")

        else:
            print("already exists")

