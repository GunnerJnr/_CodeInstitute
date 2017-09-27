# -*- coding: utf-8 -*-
"""
Tests.py:
"""
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from accounts.views import login
from accounts.models import User


# Create your tests here.
# CHALLENGE A - Create a url Test
class AccountsPageTest(TestCase):
    """
    AccountsPageTest(TestCase):
    """
    def test_account_login_page(self):
        """
        test_account_login_page():
        """
        valid_login_page = resolve('/login/')
        self.assertEqual(valid_login_page.func, login)


class CustomUserTest(TestCase):
    """
    CustomUserTest():
    """
    def test_manager_create(self):
        """
        test_manager_create():
        """
        user = User.objects._create_user(None, 'joe@bloggs.com', 'bloggs123', False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, 'bloggs123', False, False)
