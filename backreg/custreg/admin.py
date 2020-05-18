from django.contrib import admin

from .models import CustomerRegistration, CustomerPlan


class CustomerPlanAdmin(admin.ModelAdmin):
    raw_id_fields = ['customer']

admin.site.register(CustomerRegistration)
admin.site.register(CustomerPlan, CustomerPlanAdmin)
