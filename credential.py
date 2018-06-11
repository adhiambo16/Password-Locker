import pyperclip
import random

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

    @classmethod
    def credential_exist(cls,accountname):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            accountname: Accountname to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.accountname == accountname:
                    return True

        return False


    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_email(cls,accountname):
        credential_found = Credential.find_by_accountname(accountname)
        pyperclip.copy(credential_found.email)


    @classmethod
    def gen_password(cls,username):
           '''
     method that returns the credential list
           '''
        letters=username[1:4]
        num1=str(random.randit(0,9))
        num2=str(random.randit(9,16))
        gen_pass="!"num1+letters+num2+"$"+letters.upper()
        return gen_pass


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
