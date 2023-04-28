from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .models import Product

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='user1')
        cls.product1 = Product.objects.create(
            title='product1',
            description='this is descriptions for product 1',
            short_description='short description for product 1',
            price=12000,
            active=True, #show
        )
        cls.product2 = Product.objects.create(
            title='product2',
            description='this is descriptions for product 2',
            short_description='short description for product 2',
            price=13000,
            active=False, # not show
        )

    def test_post_model_str(self):
        product = self.product1
        self.assertEqual(str(product), product.title)

    def test_product_list_view_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_url_by_name(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)


    def test_product_title_on_product_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, self.product1.title)
        self.assertEqual(self.product1.description, 'this is descriptions for product 1')
        self.assertEqual(self.product1.price, 12000)

    def test_product_list_not_shown_deacive(self):
        response = self.client.get(reverse('product_list'))
        self.assertNotContains(response, self.product2.title)

