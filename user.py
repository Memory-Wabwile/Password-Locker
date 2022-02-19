# A user class to store user information
class User :
    '''
    an empty users list
    '''
    all_Users = []

    def __innit__(self, username , password):
        self.username = username 
        self.password = password

    def saveUser(self):
        User.all_Users.append(self)
        