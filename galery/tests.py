from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestCase(TestCase):

    def setUp(self):
        self.food = Category(name = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))
