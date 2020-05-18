from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CustomerRegistrationSerializer
from .models import CustomerRegistration


class CustomerRegistrationViewSet(viewsets.ModelViewSet):
    """
    List all user registrations
    """
    queryset = CustomerRegistration.objects.all()
    serializer_class = CustomerRegistrationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'email']
    ordering = ['-id']
