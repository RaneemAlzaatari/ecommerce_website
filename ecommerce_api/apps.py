from django.apps import AppConfig


class EcommerceApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce_api'


    def ready(self):
            import ecommerce_api.signals