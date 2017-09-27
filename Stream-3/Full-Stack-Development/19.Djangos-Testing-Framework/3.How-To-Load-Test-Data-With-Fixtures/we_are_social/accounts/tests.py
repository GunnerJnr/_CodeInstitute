# -*- coding: utf-8 -*-
"""
Tests.py: 
"""
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from accounts.views import login


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
