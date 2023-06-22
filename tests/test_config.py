import os
import unittest

from base_test import BaseTestCase

from src import app


class TestConfig(BaseTestCase):
    @unittest.skip("Skipping test to avoid overwrite db")
    def test_development_config(self):           
        app.config.from_object('config.DevelopmentConfig')
        assert app.config['DEBUG']
        assert not app.config['TESTING']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')


    def test_testing_config(self):
        app.config.from_object('config.TestingConfig')
        assert app.config['DEBUG']
        assert app.config['TESTING']
        assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'DATABASE_TEST_URL')
        

    @unittest.skip("Skipping test to avoid overwrite db")
    def test_production_config(self):
        app.config.from_object('config.ProductionConfig')
        assert not app.config['DEBUG']
        assert not app.config['TESTING']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'DATABASE_URL')