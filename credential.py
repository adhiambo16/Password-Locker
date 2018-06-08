class Credential:
    '''
    Class that generates new instances of credential.

    '''

    credential_list=[] #empty credential list


    @classmethod
    def find_by_accountname(cls,accountname):
            '''
            Method that takes in a accountname and returns a credential that matches that accountname.

            Args:
                password: accountname to search for
            Returns :
                Credential; of person that matches the accountname.
            '''

            for credential in cls.credential_list:
                if credential.accountname == accountname:
                    return credential






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
