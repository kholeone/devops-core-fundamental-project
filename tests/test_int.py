import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Listing, Detail

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['SECRET_KEY'] = 'test-server2'
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/e_n_v_i_/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()


    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):


    def test_add(self):
        """
        A test process of adding a listing and implementing text in the input
        """

        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)
        test_list_title='2003 E46 BMW M3'
        test_list_locationr='London, UK'
        test_list_price= 13000

        self.driver.find_element_by_xpath('//*[@id="list_title"]').send_keys(test_list_title)
        self.driver.find_element_by_xpath('//*[@id="list_location"]').send_keys(test_list_location)
        self.driver.find_element_by_xpath('//*[@id="list_location"]').send_keys(test_list_price)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

