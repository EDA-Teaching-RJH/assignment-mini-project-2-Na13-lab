import unittest
from app import Student #Imports Student class from app.py to test its functionality.

class TestSystem(unittest.TestCase):
    def test_id_validation(self): #Tests that the REGEX correctly blocks invalid IDs.
        with self.assertRaises(ValueError):
            Student("ErrorUser", "INVALID ID; missing STU prefix")
    
    def test_name_validation(self): #Tests if the Getter works. #WHY? To ensure names are being stored.
        s = Student("Test", "STU-00000")
        self.assertEqual(s.name, "Test") #Checks that the name is correctly set. 
        #WHY? To ensure that valid names are being accepted and stored properly.
        
if __name__ == "__main__"
    unittest.main()