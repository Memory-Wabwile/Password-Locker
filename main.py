from user import User
'''
importing user details
'''
from credentials import Credentials
'''
importing the users credentials
'''


def create_new_user(username,password):
    '''
    method for creating new user
    '''
    new_user=(username,password)
    return new_user

def save_user(user):
    '''
    method to save new user
    '''
    user[save_user(user)]


def delete_user(user):
    '''
    to delete a user
    '''
    user.delete_user()

def find_user(user):
    '''
    To find user
    '''
    user.find_user()

    ##end of user

    ##Beginning of credentials
def create_credentials(credentials)
    '''
    creatign new credentials
    '''
    new_credential = (account,userName,passWord)
    return new_credential






def main():
    print("WELCOME TO PASSWORD LOCKER !!")
    print('*'*50)

    while True:
        decision = input("Enter \"new\" to create a new account , \"log\" to log into an existing account or \"ex\" to exit \n").lower()
        print("\n")

        if decision == 'new':
            print("Enter your username")
            username=input()
            print("Enter your password")
            password=input()
            print("Confirm password")
            passtwo=input()

            if password == passtwo:
                print("Your passwords match")
            else: print("Your passwords do not match try again")
            

            # save_user(create_new_user(username,password))
            print('*'*50)
            print(f"Congratulations {username} your account has been created successfully")
            print('*'*50)


        elif decision == 'log':
            print("Please enter your username ")
            username = input()
            print("Enter your password")
            password = input()






if __name__ == '__main__' :
    main()
