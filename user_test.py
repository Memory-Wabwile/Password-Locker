import unittest
from user import User

class TestUser(unittest.TestCase) :

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
        self.assertEqual(self.new_user.password,"4321")


    def test_saveUser(self):
        '''
        to test if the user has been saved into the users list
        first line is for saving the new user
        '''
        self.new_user.saveUser()
        self.assertEqual(len(User.all_Users),1)


    def test_save_multiple_users(self):
        '''
        test to check if we can save multiple users
        create test_user object to save the users
        '''
        self.new_user.saveUser()
        test_user = User("Fabiana" , "9876")
        test_user.saveUser()
        self.assertEqual(len(User.all_Users),2)


    



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

