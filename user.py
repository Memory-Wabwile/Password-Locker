# A user class to store user information
class User 

    all_Users[]

    def __innit__(self, username , password)
        self.username = username 
        self.password = password

    def saveUser(self)
        User.all_Users.append(self)
        