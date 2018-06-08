class User:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty contact list

     # Init method
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def __init__(self,username,password,email):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        self.email = email
