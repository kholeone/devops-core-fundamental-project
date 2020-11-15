import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Listing, Detail

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY='sdfijsdiofsdjf',
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree
        listingtest = Listing(list_title = "Nike Air Jordan 1 High", list_location = "London, UK", list_price = 339)
        detailtest  = Detail(listing_id = 1, detail_description = "One of the best shoes ever, limited release..will go fast!", detail_category = "clothes")

        # save users to database
        db.session.add(listingtest)
        db.session.commit()
        db.session.add(detailtest)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_index_get(self):

        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code,200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code,200)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,302) 

    def test_detail_get(self):
        response = self.client.get(url_for('detail'))
        self.assertEqual(response.status_code,200) 

    def test_add_detail_get(self):
        response = self.client.get(url_for('add_detail'))
        self.assertEqual(response.status_code,200)
   
    def test_update_detail_get(self):
        response = self.client.get(url_for('update_detail'))
        self.assertEqual(response.status_code,302)


