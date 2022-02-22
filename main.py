from user import User           #importing user details
from credentials import Credentials #importing the users credentials



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
    user.save_user(user)


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
def create_credentials(account,userName,passWord):
    '''
    creating new credentials
    '''
    new_credential = Credentials(account,userName,passWord)
    return new_credential


def save_credentials(credential):
    '''
    to save the new credentials
    '''
    credential.save_credentials()


def delete_credentials(credential):
    '''
    to delete a exissting credential from the list
    '''
    return credentials.delete_credentials(credentials)


def display_credentials():
    '''
    to display the credentials
    '''
    return Credentials.display_credentials()


def find_credentials(account):
    '''
    to find a specific credential account
    '''
    return Credentials.find_credentials(account)

def random_password():
    '''
    generates a random password
    '''
    password = Credentials.randomPassword("string")
    return password


def main():
    print("WELCOME TO PASSWORD LOCKER !!")
    print('*'*50)

    while True:
        decision = input("Enter \"new\" to create a new account , \"log\" to log into an existing account or \"ex\" to exit \n").lower()
        print("\n")

        if decision == 'new':
            print("Enter your username")
            username=input()
            passsword= input("Enter \"own\" to write your own password and \"gen\" to generate a random password \n")
            if passsword == "own":
                print("Enter your password")
                password=input()
                print("Confirm password")
                passtwo=input()
            
                if password == passtwo:
                    print("Your passwords match")
                else: print("Your passwords do not match try again")

            elif passsword == "gen":
                password = random_password()
                print(f"Your password is {password}")

            # save_user(create_new_user(username,password))
            print('*'*50)
            print(f"Congratulations {username} your account has been created successfully")
            print('*'*50)


        elif decision == 'log':
            print("Please enter your username ")
            username = input()
            print("Enter your password")
            password = input()
            print(f"Welcome back {username} to password Locker")
            print('*'*100)


        elif decision == 'ex': 
            break


        while True:
            print("\n")
            cred = input("Enter \"nc\"to create a new credential , \"dc\"  to display credentials and \"x\" to go back to first step \n").lower()
            print("\n")

            if cred == 'nc':
                print("Enter the name of the site you want to save password for")
                account = input()
                print("Enter your username of the site")
                userName = input()
                print("Enter a password \n")
                passWord = input()
                print("Confirm the password")
                passstwo = input()

                if passWord == passstwo:
                    print("Your passwords match")
                    
                else: print("Your passwords do not match try again")
                    
                save_credentials(create_credentials(account,userName,passWord))
                
                print('*'*50)
                print(f"You have successfully saved your credentials for {account}")
                print('*'*100)


            elif cred == 'dc':
                print ("Your details are as follows")
                if display_credentials():
                    for account in display_credentials():
                        print(f"For {account.account}  account , Your username is : {userName} and Password : {passWord}")
                else :
                    print("Ivalid credentials")

            elif cred == 'x': 
                break




if __name__ == '__main__' :
    main()
