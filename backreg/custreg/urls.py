from django.urls import include, path
from rest_framework import routers
from .views import CustomerRegistrationViewSet

router = routers.DefaultRouter()

router.register(r'registrations', CustomerRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls))
]