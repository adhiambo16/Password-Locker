import unittest # Importing the unittest module
from credential import Credential # Importing the contact class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the class credential behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

      # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("facebook","0702769629","adhiambolydia96@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.accountname,"facebook")
        self.assertEqual(self.new_credential.password,"0702769629")
        self.assertEqual(self.new_credential.email,"adhiambolydia96@gmail.com")


if __name__ == '__main__':
    unittest.main()
