
from django import forms
from .models import UserCompanyModel
class UpdateCompanyForm(forms.ModelForm):
    
    class Meta:
        model= UserCompanyModel
        fields = ("company_name", 'dot_number')
