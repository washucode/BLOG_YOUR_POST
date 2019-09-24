import unittest
from app.models import Quotes

class testQuotes(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quotes('ESther','Coding can be fun',"http://github.com/washucode")

    def test_instance_variables(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))