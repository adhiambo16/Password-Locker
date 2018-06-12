
from credential import Credential
from Userlogin import User

#credential function
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


#user function

def create_user(username,password,email):
    '''
    Function to create a new user
    '''
    new_user = User(username,password,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def gen_password(username):
    return Credential.gen_password(username)



def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return find_User_user(username)

def check_existing_user(username):
    '''
    Function that check if a user exists with that username
    '''
    return User.user_exist(username)



def main():
    print("Welcome")
    print('-'*20)

    while True:
        print ("Use these short codes")
        print ("cc - create acc, lo -login, ex - exit app")
        short_code = input().lower
        if short_code == 'cc':

            print("New User")
            print("-"*10)

            print ("Username ....")
            Username = input()

            print("Password ...")
            password = input()

            print("Email address ...")
            Email = input()
            print ('\n')


            save_user(user(username,password,email))
            # print (f"\nNew User {username} created")

        elif short_code == 'lo':
            print("login to your account")
            print("-"*10)

            print("username....")
            search_user = input()
            if check_existing_user(search_user):
                user_find = find_user(search_user)

                print("input password....")
                password = input()
            if password == input():
                print (f"Welcome {username} logged in")
                print ('\n')

    while True:
        print("Use these short codes")
        print("""
        cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list
        """)
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

            password=gen_password(username)
            print(f"Your password is{password}")
            save_new_credential(create_credential((accountname,password,e_address))) # create and save new credential.
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
                print(f"{search_credential.accountname}")
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
