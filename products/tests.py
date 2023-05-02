from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User
from products.models import Product


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index') # '127.0.0.1:8000/'
        response = self.client.get(path)
        print(response)

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'products/index.html')
        # self.assertEqual(response.context_data['title'],'Store') #пропустил несоклько уроков, этот код не работает


# Create your tests here.
class ProductsListViewTestCase(TestCase):

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'products/products.html')
       # self.assertEqual(response.context_data['title'], 'Store - Каталог')
