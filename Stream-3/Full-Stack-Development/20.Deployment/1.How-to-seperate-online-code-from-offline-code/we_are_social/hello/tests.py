# -*- coding: utf-8 -*-
"""
Test.py:
"""
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from hello.views import get_index
from accounts.models import User


# Create your tests here.
class HomePageTest(TestCase):
    """
    HomePageTests():
    """
    fixtures = ['subjects', 'user']

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='joebloggs')
        self.user.set_password('bloggs123')
        self.user.save()
        self.login = self.client.login(username='joebloggs', password='bloggs123')
        self.assertEqual(self.login, True)

    def test_home_page_resolves(self):
        """
        test_home_page_resolves():
        """
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_ok(self):
        """
        test_home_page_status_code_is_ok():
        """
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        """
        test_check_content_is_correct():
        """
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)
