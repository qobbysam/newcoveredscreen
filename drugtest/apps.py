from django.apps import AppConfig

from userapplication.signals import create_purchase_drugtest

class DrugtestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drugtest'


    def ready(self):
        
        from drugtest import signals

        create_purchase_drugtest.connect(signals.create_purchse_drugtest)