from django.apps import AppConfig
from userapplication.orderhandler import create_purchase_consortium

class ConsortiumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consortium'

    def ready(self):
        from consortium import signals

        create_purchase_consortium.connect(signals.create_purchase_consortium)