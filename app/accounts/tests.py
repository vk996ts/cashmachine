# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from selenium import webdriver


from django.test import LiveServerTestCase


class AdminTest(LiveServerTestCase):
    """
    Simple test for admin and auth
    """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

    def test_auth(self):
        self.browser.get('http://localhost:8000/')
        body = self.browser.find_element_by_tag_name('body')
        assert 'Enter Card Number' in body.text

        card_number = '1111222233334444'
        for d in card_number:
            button1 = body.find_element_by_id('btn{}'.format(d))
            button1.click()
        OK = body.find_element_by_id('btnOK')
        OK.click()

        body = self.browser.find_element_by_tag_name('body')
        assert 'Enter PIN' in body.text

        PIN = '1234'
        for d in PIN:
            button1 = body.find_element_by_id('btn{}'.format(d))
            button1.click()
        OK = body.find_element_by_id('btnOK')
        OK.click()

        body = self.browser.find_element_by_tag_name('body')
        assert 'Operations' in body.text