from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import CustomerRegistration, CustomerPlan


class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = ('id', 'name', 'billing_interval', 'frequency', 'currency')


class CustomerRegistrationSerializer(CountryFieldMixin, serializers.ModelSerializer):
    plans = CustomerPlanSerializer(many=True, required=False)

    class Meta:
        model = CustomerRegistration
        fields = ('id', 'first_name', 'last_name', 'email', 'country_code', 'plans')
