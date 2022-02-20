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



def main():
    print("Welcome to password Locker")

if __name__ == '__main__' :
    main()
