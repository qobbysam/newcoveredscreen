import os

from django.contrib.auth import get_user_model

from django.conf import settings
from oscar.apps.partner.importers import CatalogueImporter


User = get_user_model()

def createAdminUser():
    print("creatinf admin user")

    username = os.environ.get('FIRST_ADMIN_USERNAME')
    email = os.environ.get('FIRST_ADIMIN_EMAIL')
    password = os.environ.get('FIRST_ADMIN_PASSWORD')

    try:
        su = User.objects.create_superuser(username=username, email=email, password=password)

        su.save()
    except:
        print("user already exists")


def createProductTypes():
    print("creating product types")

    if settings.IMPORT_CATALOGUE_PATH is not None:
        print("starting imports")

        im = CatalogueImporter()

        im.handle(file_path=settings.IMPORT_CATALOGUE_PATH)


    else:
        print("no import file given")

def createDefaultPages():
    print("creating default pages")