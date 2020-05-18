from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomerRegistration
from .tasks import get_plans_for_new_user


@receiver(post_save, sender=CustomerRegistration)
def get_plans(sender, instance, created, **kwargs):
    if created:
        # We only want to run this once at creation time
        get_plans_for_new_user.delay(instance.pk, instance.country_code.code)
