# A user class to store user informationer
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

    def delete_user(self):
        '''
        delete method deletes user details from saved account list
        '''
        User.all_Users.remove(self)

        @classmethod
        def find_user(cls,username):
            for user in cls.all_Users:
                if user.username == username:
                    return user

        