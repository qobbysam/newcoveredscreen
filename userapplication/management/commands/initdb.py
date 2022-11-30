import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from .actions import createAdminUser, createProductTypes, createDefaultPages

class Command(BaseCommand):

    def handle(self, *args, **options):

        

        try:
            createAdminUser()
        
        except:

            print("create default admin done already", )

        try:
            createProductTypes()
        except:
            print("product types already exist")


        try:
            createDefaultPages()
        
        except:
            print("default pages exist already")


