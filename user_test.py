import unittest
from user import User

class Test_User(unittest.TestCase) :

    '''
        Test class that defines test cases for the users
        unittest.TestCase helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases
        create user object
        '''
        self.new_user = User("Memory" , "1234")   

    def test__init__(self): 
        '''
        to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Memory")
        self.assertEqual(self.new_user.password,"1234")



if __name__ == '__main__' :
    unittest.main()


    # def create_account(self,username, password): 
    #     if decision == "new" :
    #         print("Enter Username")
    #         self.username = input()
    #         return True
    #     else : return False 

    # def exit(decision):
    #     if decision == "ex": return True
    #     else : return False
            
    # while True :
    #     print("Welcome to password Locker")
    #     decision = input("Type \"new\" to create a new account , \"log\" to log into an existing account or \"ex\" to exit \n").lower()
    #     print("\n")
    #     if exit(decision):break

