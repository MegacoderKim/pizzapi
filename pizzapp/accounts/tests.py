from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Customer

class CustomerAccountTests(APITestCase):

    def test_create_account(self):

        url = reverse('customer-list')
        data = {'username': 'pizzaman','email':'pizzman@pizzapi.de'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().username, 'pizzaman')
