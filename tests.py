import unittest
import os
from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_multi(self):
        self.app.get('/')
        assert "Use proper URLs"

    def test_404(self):
        self.app.get('/random_url')
        assert "Use proper URLs"

    def test_404_single(self):
        self.app.get('/random_url/another')
        assert "Use proper URLs"

    def test_404_double(self):
        self.app.get('/random_url/another/yet_another')
        assert "Use proper URLs" 

    def test_single_form(self):
        self.app.get('/chainsaw/Mike_tester/Jack_tester')
        assert '''Fuck me gently with a chainsaw, jack_tester. 
                Do i look like Mother Teresa? - mike_tester'''

    def test_double_form(self):
        self.app.get('/this/Mike_tester')
        assert "Fuck this - mike_tester"


if __name__ == "__main__":
    unittest.main()
