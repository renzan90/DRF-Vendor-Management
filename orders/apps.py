from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self, *args, **kwargs):
        from django.db.models.signals import pre_save
        from .signals import presave_delivery_date

        model = self.get_model('PurchaseOrder')

        pre_save.connect(presave_delivery_date, sender=model)