# from _typeshed import Self
from django.http import response
from django.urls import reverse, resolve
from django.test import TestCase, Client
from store.views import store, cart, checkout, updateItem, processOrder
from store.models import Customer, Product, Order
import json

class TestUrls(TestCase):
    def testStore(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def testCart(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)

    def testCheckout(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def testUpdateItem(self):
        url = reverse('update_item')
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateItem)

    def testProcessOrder(self):
        url = reverse('process_order')
        print(resolve(url))
        self.assertEquals(resolve(url).func, processOrder)

class TestViews(TestCase):
    
    def test1(self):
        customer = Client()
        response = customer.get(reverse('store'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')

    def test2(self):
        customer = Client()
        response = customer.get(reverse('cart'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')

    def test3(self):
        customer = Client()
        response = customer.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')
