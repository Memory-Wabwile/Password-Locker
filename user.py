# A user class to store user information
class User :
    '''
    an empty users list
    '''
    all_Users = []

    def __innit__(self, username , password):
        '''
        define properties for the objects
        '''
        self.username = username 
        self.password = password

   
    def saveUser(self):
        '''
        save user method saves users into all users list
        '''
        User.all_Users.append(self)
        