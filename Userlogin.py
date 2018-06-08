class userlogin:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty contact list

    def __init__(self,username,password,email):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        self.email = email
