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
        Set up method to run before each test cases.find_by_accountname
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

    def test_find_credential_by_accountname(self):
        '''
        test to check if we can find a credential by accountname and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("facebook","0712345678","adhiambolydia96@gmail.com") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_accountname("facebook")

        self.assertEqual(found_credential.email,test_credential.email)



    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("facebook","0712345678","adhiambolydia96@gmail.com") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("facebook")

        self.assertTrue(credential_exists)



    def test_display_all_credential(self):
        '''
        method that returns a list of all credential saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found credential
    #     '''
    #
    #     self.new_credential.save_credential()
    #     Credential.copy_email("0712345678")
    #
    #     self.assertEqual(self.new_credential.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
