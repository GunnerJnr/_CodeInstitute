# -*- coding: utf-8 -*-
"""
Tests.py:
"""
from __future__ import unicode_literals

from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import resolve
from django import forms

from accounts.forms import UserRegistrationForm
from accounts.models import User
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

    def test_registration_form(self):
        """
        test_registration_form():
        """
        form = UserRegistrationForm({
            'email': 'joe@bloggs.com',
            'password1': 'bloggs123',
            'password2': 'bloggs123',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_missing_email(self):
        """
        test_registration_form():
        # POSSIBLE BUG IN HERE WHILE TESTING ??
        self.assertFalse(form.is_valid())
            AssertionError: True is not false
        """
        form = UserRegistrationForm({
            'password1': 'bloggs123',
            'password2': 'bloggs123',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_missing_password1(self):
        """
        test_registration_form():
        """
        form = UserRegistrationForm({
            'email': 'joe@bloggs.com',
            'password2': 'bloggs123',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your password",
                                 form.full_clean())

    def test_registration_form_fails_missing_password2(self):
        """
        test_registration_form():
        """
        form = UserRegistrationForm({
            'email': 'joe@bloggs.com',
            'password1': 'bloggs123',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please re-enter your password",
                                 form.full_clean())

    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'joe@bloggs.com',
            'password1': 'bloggs123',
            'password2': 'bloggs132',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())
