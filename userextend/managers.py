from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from userextend  import signals

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, username,password,account_type, company_dot, company_name , full_name, phone_number ,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        full_decom = full_name.split(" ")

        user.first_name = full_decom[0]
        user.last_name =  " ".join(full_decom[1:])
        user.phone = phone_number
        user.save()

        company = {}
        company['account_type'] =  account_type
        company['dot_number'] = company_dot
        company['company_name'] = company_name
        # company['company_user'] = user 
        company['is_company'] =  self.is_company(account_type)

        self.notifyall(user, company)

        return user

    def is_company(self, account_type) -> bool:
        return account_type != 'NC'

    def create_superuser(self, email,username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def notifyall(self, user, company):
        signals.user_registered_company.send_robust(sender=self, user=user, company=company)
    

        