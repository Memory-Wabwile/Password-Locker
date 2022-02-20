import unittest
'''
importing the unittest module
'''
from credentials import Credentials
'''
import class Credentials
'''

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test cases
        
        '''
        self.new_credential = Credentials('Instagram' , 'Memory' , '4321')  


    def test__init__(self): 
        '''
        to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.userName,'Memory')
        self.assertEqual(self.new_credential.passWord,'4321')


    def test_save_credentials(self):
        '''
         to test if the user has been saved into the users list
        first line is for saving the new credentials
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


    def tearDown(self):
        '''
        tearDown method does clean up after each test case
        '''
        Credentials.credentials_list=[]


    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("Twitter" ,"Nimo", "1234")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credentials(self):
        '''
        the delete credentials method deletes credentials from the credentials list"
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("Twitter" ,"Nimo", "1234")
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    
    def test_display_credentials(self):
        '''
        test to display the credentials iiin the credentials list
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


    def 

    
if __name__ == '__main__' :
    unittest.main()
