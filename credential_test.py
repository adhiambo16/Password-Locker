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

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),


if __name__ == '__main__':
    unittest.main()
