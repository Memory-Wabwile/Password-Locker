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


if __name__ == '__main__' :
    unittest.main()
