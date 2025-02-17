from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from appstore.models import App

class AppCreationTestCase(APITestCase):

    def setUp(self):
        """Create a test user and authenticate"""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        self.token = self.client.post("/api/token/", {"username": "testuser", "password": "password123"}).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_create_app_valid_data(self):
        """Test creating an app with valid data"""
        response = self.client.post("/api/apps/", {
            "title": "Test App",
            "description": "This is a test app",
            "price": 9.99
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 1)

    def test_create_app_invalid_data(self):
        """Test creating an app with missing fields"""
        response = self.client.post("/api/apps/", {
            "title": "",  # Title should not be empty
            "price": -5  # Price should be positive
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AdminVerificationTestCase(TestCase):

    def setUp(self):
        """Create an admin user, a normal user, and a test app"""
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")
        self.normal_user = User.objects.create_user(username="testuser", password="password123")

        self.app = App.objects.create(
            title="Unverified App",
            description="Test app",
            price=5.99,
            status="pending",
            owner=self.normal_user
        )

    def test_admin_can_access_app_list(self):
        """Test that an admin can access the app list in the Django admin"""
        self.client.login(username="admin", password="admin123")
        response = self.client.get(reverse('admin:appstore_app_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_admin_can_verify_app_in_admin(self):
        """Test that an admin can verify an app through the Django admin"""
        self.client.login(username="admin", password="admin123")

        # Django Admin action to verify the app
        response = self.client.post(reverse('admin:appstore_app_changelist'), {
            'action': 'verify_apps',  # Custom admin action defined earlier
            '_selected_action': [self.app.id],
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        # Check if the app's status was updated to "verified"
        self.app.refresh_from_db()
        self.assertEqual(self.app.status, 'verified')

    def test_non_admin_cannot_access_admin(self):
        """Test that a normal user cannot access the Django admin"""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('admin:appstore_app_changelist'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_admin_can_reject_app(self):
        """Ensure the admin action rejects the app correctly."""
        self.client.login(username="admin", password="admin123")

        # Simulate the 'reject_apps' action
        response = self.client.post(reverse('admin:appstore_app_changelist'), {
            'action': 'reject_apps',
            '_selected_action': [self.app.id]
        })

        self.app.refresh_from_db()
        self.assertEqual(self.app.status, 'rejected')
        self.assertEqual(response.status_code, 302)  # Successful action redirects
