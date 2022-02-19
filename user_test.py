import unittest
from user import User

class Test_User(unittest.TestCase) :

    def create_account(self,username, password): 
        if decision == new :
            print("Enter Username")
            username = input()
            return True


        while True :
            print("Welcome to password Locker")
            print("\n")
            print("Type \"new\" to create a new account , \"log\" to log into an existing account or \"ex\" to exit")
            decision = input().lower()
            print("\n")

if __name__=="__main__":
    unittest.main()
