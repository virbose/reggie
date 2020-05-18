from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomerRegistration, CustomerPlan


# Models

class CustomerRegistrationTest(TestCase):

    def setUp(self) -> None:
        """ Create a new customer registration object to be used in tests """
        CustomerRegistration.objects.create(
            first_name='Joe',
            last_name='Bloggs',
            email='joe@bloggs.com',
            country_code='GB')

    def test_string_repr(self) -> None:
        """ Make sure we are retrieving the correct string representation for the object """
        new_reg = CustomerRegistration.objects.get(email='joe@bloggs.com')
        self.assertEqual(str(new_reg), f'{new_reg.first_name} {new_reg.last_name} - {new_reg.email}')

    def test_bad_email(self) -> None:
        """ Ensure we can't submit a bad email format """
        with self.assertRaises(ValidationError):
            CustomerRegistration.objects.create(
                first_name='Joe',
                last_name='Bloggs',
                email='invalidemail',
                country_code='GB'
            )

    def test_bad_country_code(self) -> None:
        """Ensure the model doesn't save with an invalid country code """
        with self.assertRaises(ValidationError):
            CustomerRegistration.objects.create(
                first_name='Joe',
                last_name='Bloggs',
                email='somemeail@email.com',
                country_code='BAD_COUNTRY_CODE'
            )


class CustomerPlanTest(TestCase):

    def setUp(self) -> None:
        """ Create a new customer registration object to be used in tests """
        CustomerRegistration.objects.create(
            first_name='Joe',
            last_name='Bloggs',
            email='joe@bloggs.com',
            country_code='GB'
        )

    def test_string_repr(self) -> None:
        """ Make sure we are retrieving the correct string representation for the object """
        related_user_reg = CustomerRegistration.objects.first()
        new_plan = CustomerPlan.objects.create(
            customer=related_user_reg,
            name='Testname',
            billing_interval='MONTH',
            frequency='Monthly',
            currency='GBP'
        )
        self.assertEqual(str(new_plan), f'Plan {new_plan.pk} for {new_plan.customer} - {new_plan.name}')

    def test_bad_billing_interval_choice(self) -> None:
        """
        Ensures that trying to create a plan object with an invalid billing interval raises an error
        """
        related_userreg = CustomerRegistration.objects.first()
        with self.assertRaises(ValidationError):
            CustomerPlan.objects.create(
                customer=related_userreg,
                name='Testname',
                billing_interval='invalid-interval',
                frequency='Monthly',
                currency='GBP'
            )


# REST API Viewset


class RegistrationsViewsetTest(APITestCase):

    def setUp(self) -> None:
        """ Resolve the url for following tests"""
        self.url = reverse('customerregistration-list')

    def test_get_registrations(self) -> None:
        """ Ensure we can query and get a list of all registrations """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_correct_registration(self) -> None:
        """
        Ensure we can succesfully save a new object
        """
        test_data = {
            "first_name": "Joe",
            "last_name": "Blogs",
            "email": "test@email.com",
            "country_code": "GB"
        }
        response = self.client.post(self.url, data=test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_obj = response.json()
        self.assertEqual(CustomerRegistration.objects.filter(pk=new_obj.get('id')).count(), 1)

    def test_post_duplicate_email_registration(self) -> None:
        """ Ensure we cannot save an object with the same email"""
        dupe_test_data  = {
            "first_name": "Joe",
            "last_name": "Duplicate",
            "email": "testdupe@email.com",
            "country_code": "AU"
        }
        response = self.client.post(self.url, data=dupe_test_data, format='json')
        # Ensure the first obj is created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Try again with the same data
        dupe_resp = self.client.post(self.url, data=dupe_test_data, format='json')
        self.assertEqual(dupe_resp.status_code, status.HTTP_400_BAD_REQUEST)
        err_data = dupe_resp.json()
        self.assertDictEqual(err_data, {"email": ["customer registration with this email already exists."]})

    def test_post_bad_email_registration(self) -> None:
        """ Ensure we cannot save an object with bad post data"""
        bad_test_data  = {
            "first_name": "Joe",
            "last_name": "Blogs",
            "email": "bademailaddr",
            "country_code": "GB"
        }
        response = self.client.post(self.url, data=bad_test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_bad_country_code_registration(self) -> None:
        """ Ensure we cannot save an object with bad post data"""
        bad_test_data  = {
            "first_name": "Joe",
            "last_name": "Blogs",
            "email": "test1@email.com",
            "country_code": "badCOUNTRYdata"
        }
        response = self.client.post(self.url, data=bad_test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        resp_data = response.json()
        self.assertTrue('country_code' in resp_data)
