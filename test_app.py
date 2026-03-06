import unittest
from app import Student #Imports Student class from app.py to test its functionality.

class TestSystem(unittest.TestCase):
    def test_id_validation(self): #Tests that the REGEX correctly blocks invalid IDs.
        with self.assertRaises(ValueError):
            Student("ErrorUser", "INVALID ID; missing STU prefix")