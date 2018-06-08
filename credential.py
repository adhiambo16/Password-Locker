class Credential:
    '''
    Class that generates new instances of credential.

    '''

    credential_list=[] #empty credential list

    def __init__(self,accountname,password,email):

        #docstring removed

        self.accountname = accountname
        self.password = password
        self.email = email
