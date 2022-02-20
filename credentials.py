class Credentials :
    '''
    A credentials class to store all the user information and creation of new instances
    '''
    credentials_list=[]

    
    @classmethod
    def user_verification(cls , username , password):
        '''
        method to verify if user is in the all users list
        '''
        verified_user=""
        for user in User.all_users:
            if(user.username == username  and user.password == password):
                verified_user == user.username
        return verified_user


    def __innit__(self,userName,passWord):


    