import unittest
from user import User

class Test_User(unittest.TestCase) :

    def create_account(self,username, password): 
        if decision == "new" :
            print("Enter Username")
            self.username = input()
            return True
        else : return False 

    def exit(decision):
        if decision == "ex": return True
        else : return False
            
    while True :
        print("Welcome to password Locker")
        decision = input("Type \"new\" to create a new account , \"log\" to log into an existing account or \"ex\" to exit \n").lower()
        print("\n")
        if exit(decision):break

if __name__=="__main__":
    unittest.main()
