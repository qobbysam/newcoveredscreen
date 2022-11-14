from django.apps import AppConfig
from oscar.apps.order.signals import order_placed
from .signals import  order_placed_receiver

class UserapplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapplication'

    def ready(self):

        order_placed.connect(order_placed_receiver)
        