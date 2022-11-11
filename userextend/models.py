from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from userextend.managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)

    phone = models.CharField(verbose_name='phone',blank=True, null=True, max_length=30)
    profile_pic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    default_company_name = models.CharField(max_length=200, blank=True, null=True)
    default_company_key = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email