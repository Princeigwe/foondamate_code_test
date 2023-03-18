from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class QueryTest(APITestCase):
    def test_response_status_code(self):
        params = {'math_query': "2x+7=9"}
        url = reverse('math_query')
        response = self.client.get(url, params=params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)