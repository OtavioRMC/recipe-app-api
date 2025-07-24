"""
Test for the Django admin modifications.
Unit test suite for checking Django admin interface for users is working
properly.

Unit tests
1. if users show up in the Django Admin list page.
2. if the edit user page loads correctly
3. if the create user page loads correctly.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
  """Tests for Django Admin."""

  def setUp(self):
    """Create user and client."""
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser(
      email="admin@example.com",
      password="testpass123",
    )

    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
      email="user@example.com",
      password='testpass123',
      name='Test User'
    )

  def test_users_list(self):
    """Test that users are listed on page."""
    url = reverse('admin:core_user_changelist')
    res = self.client.get(url)

    self.assertContains(res, self.user.name)
    self.assertContains(res, self.user.email)

  def test_edit_user_page(self):
    """Test the edit user page works."""
    url = reverse('admin:core_user_change', args=[self.user.id])
    res = self.client.get(url)

    self.assertEqual(res.status_code,200)

  def test_create_user_page(self):
    """Test the create user page works."""
    url = reverse('admin:core_user_add')
    res = self.client.get(url)

    self.assertEqual(res.status_code,200)