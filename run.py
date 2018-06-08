#!/usr/bin/env python3.6
from credential import Credential
from Userlogin import User 


def create_credential(accountname,password,email):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(accountname,password,email)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    contact.save_credendial()



def find_credential(accountname):
    '''
    Function that finds a credential by accountname and returns the credential
    '''
    return Credential.find_by_accountname(accountname)

def check_existing_credential(accountname):
    '''
    Function that check if a credential exists with that accountname and return a Boolean
    '''
    return Credential.credential_exist(accountname)


def display_credential():
    '''
    Function that returns all the saved credential
    '''
    return Credential.display_credential()



def main():
    print("Hey Welcome to your credential list. What is your accountname?")
    accountname = input()

    print(f"Hey {accountname}. what would you like to check?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("Accountname ....")
                            accountname = input()



                            print("Password ...")
                            password = input()

                            print("Email address ...")
                            e_address = input()


                            save_credential(create_credential((accountname,password,e_address)) # create and save new credential.
                            print ('\n')
                            print (f"New Credential {accountname} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credential():
                                    print("Here is a list of all your credential")
                                    print('\n')
                                    for credential in display_credential():
                                            print(f"{credential.accountname} .....{credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credential saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the password you want for")

                            search_password = input()
                            if check_existing_credential(search_password):
                                    search_credential = find_credential(search_password)
                                    print(f"{search_credential.accountname}
                                    print('-' * 20)

                                    print(f"password.......{search_credential.password}")
                                    print(f"Email address.......{search_credential.email}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()
