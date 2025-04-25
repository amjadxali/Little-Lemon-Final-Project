from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a new instance of the Menu model
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        
        # Compare the string representation of the object with the anticipated value
        self.assertEqual(str(item), "IceCream : 80")