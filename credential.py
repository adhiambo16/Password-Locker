class Credential:
    '''
    Class that generates new instances of credential.

    '''

    credential_list=[] #empty credential list
    # Init method
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def __init__(self,accountname,password,email):

        #docstring removed

        self.accountname = accountname
        self.password = password
        self.email = email
