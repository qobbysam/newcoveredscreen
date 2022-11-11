from django.apps import AppConfig
from userextend.signals import user_registered_company

class CompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'

    def ready(self):
        from company import signals

        user_registered_company.connect(signals.create_company)

