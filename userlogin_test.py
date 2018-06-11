import unittest # Importing the unittest module
from  Userlogin import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

       # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("adhiambo16","katelyne3","adhiambolydia96@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"adhiambo16")
        self.assertEqual(self.new_user.password,"katelyne3")
        self.assertEqual(self.new_user.email,"adhiambolydia96@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)




            # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

                # Items  here...

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","0712345678","test@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","0712345678","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_username("Test")

        self.assertEqual(found_user.email,test_user.email)





    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","0712345678","test@user.com") # new user
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)




if __name__ == '__main__':
    unittest.main()
