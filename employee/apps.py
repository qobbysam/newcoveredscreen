from django.apps import AppConfig

from userapplication.signals import create_employee_signal
from .signals import handle_create_employee

class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee'

    def ready(self):

        create_employee_signal.connect(handle_create_employee)

