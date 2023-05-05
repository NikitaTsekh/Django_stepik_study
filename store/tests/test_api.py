from rest_framework.test import APITestCase
from django.urls import reverse
from products.models import Product, ProductCategory


class ProductsApiTestCase(APITestCase):
    def test_get(self):
        category_1 = ProductCategory.objects.create(name="Обувь")
        product_1 = Product.objects.create(name="Сандалии", description='Элегантные летные женские сандалии',
                                           price=10000, quantity=10, category=category_1)
        # product_2=Product.objects.create(name = "Шлепанцы", description='Элегантные летные женские шлепанцы', price=10000, quantity=10,category=)

        # name = models.CharField(max_length=256)
        # description = models.TextField()
        # price = models.DecimalField(max_digits=8, decimal_places=2)
        # quantity = models.PositiveIntegerField(default=0)
        # image = models.ImageField(upload_to='products_images', null=True, blank=True)
        # category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
        url = reverse('index')
        print(url)
        response = self.client.get(url)
        print(response)
