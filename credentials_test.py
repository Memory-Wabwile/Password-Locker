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
        self.new_user = Credentials('Instagram' , 'Memory' , '4321')   


