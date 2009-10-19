"""
Tests for the cmsplugin_news app
"""

from django.test import TestCase

class NewsTest(TestCase):
    def setUp(self):
        pass  
        
    def tearDown(self):
        pass
        
    def test_unpublished(self):
        """
            Test if unpublished items are hidden by default
        """
        pass
        
    def test_future_published(self):
        """
            Tests that items with a future published date are hidden
        """
        pass
        
    def test_navigation(self):
        """
            Tests if the navigation build by navigation.get_nodes is correct
        """
        pass
