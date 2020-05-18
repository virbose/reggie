from django.apps import AppConfig


class CustregConfig(AppConfig):
    name = 'custreg'
    verbose_name = 'Customer Registration'

    def ready(self):
        import custreg.signals
