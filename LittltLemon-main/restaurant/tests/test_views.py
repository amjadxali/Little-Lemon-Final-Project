from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token  # Import Token model
from django.contrib.auth.models import User  # Import User model

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Generate a token for the user
        self.token = Token.objects.create(user=self.user)
        
        # Add a few test instances of the Menu model
        self.menu1 = Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory=20)
        self.menu3 = Menu.objects.create(title="Pasta", price=10.99, inventory=15)
        
        # Initialize APIClient for testing API endpoints
        self.client = APIClient()
        
        # Authenticate the client using the token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get(reverse('menu-items'))  # Replace 'menu-list' with your URL name
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)

        # Assert the response status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_menus.data)
