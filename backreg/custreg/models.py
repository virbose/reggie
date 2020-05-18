from django.db import models
from django_countries import fields as djcountry_fields


class CustomerRegistration(models.Model):
    first_name = models.CharField(max_length=120, help_text='First Name', default=None)
    last_name = models.CharField(max_length=120, help_text='First Name', default=None)
    email = models.EmailField(max_length=254, help_text='Email Address', unique=True, default=None)
    country_code = djcountry_fields.CountryField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.email}'

    def save(self, *args, **kwargs) -> None:
        # From https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.full_clean
        # calling .save() doesn't invoke the email validation automatically via full_clean().
        # Because we're mainly going to be creating these objs via an API, it's best to override the save()
        # method to do so
        self.full_clean()
        super().save(*args, **kwargs)


class CustomerPlan(models.Model):
    customer = models.ForeignKey('CustomerRegistration', on_delete=models.CASCADE, related_name='plans', default=None)
    name = models.CharField(max_length=120, help_text='Name of Plan', default=None)
    billing_interval = models.CharField(
        max_length=20,
        choices=(
            ("MONTH", "Monthly"),
            ("YEAR", "Yearly")
        ),
        help_text='Billing Interval',
        default=None
    )
    frequency = models.CharField(max_length=120, help_text='Invoice Frequency', default=None)
    currency = models.CharField(max_length=3, help_text='Cost Currency', default=None)

    def __str__(self) -> str:
        return f'Plan {self.pk} for {self.customer} - {self.name}'

    def save(self, *args, **kwargs) -> None:
        # From https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.full_clean
        # calling .save() doesn't invoke the email validation automatically via full_clean().
        # Because we're mainly going to be creating these objs via an API, it's best to override the save()
        # method to do so
        self.full_clean()
        super().save(*args, **kwargs)
