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
        self.assertEqual(len(Credential.credential_list),1),

        # Items up here...

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential= Credential("twitter","0712345678","Moringaschool123") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

# other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("facebook","0712345678","Moringaschool123") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
    def test_find_credential_by_password(self):
        '''
        test to check if we can find a credential by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("facebook","0711223344","Moringaschool123") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_password("0711223344")

        self.assertEqual(found_credential.email,test_credential.email)

    @classmethod
    # def find_by_password(cls,password):
    #     '''
    #     Method that takes in a password and returns a credential that matches that password.
    #
    #     Args:
    #         password: Password to search for
    #     Returns :
    #         Credential; of person that matches the password.
    #     '''
    #
    #     for credential in cls.credential_list:
    #         if credential.password == password:
    #             return credential


if __name__ == '__main__':
    unittest.main()
