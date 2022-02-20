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


    def __init__(self,account,userName,passWord):
        '''
        define properties for the objects where credentials will be stored
        '''
        self.account = account
        self.userName = userName
        self.passWord =passWord


    def save_credentials(self):
        '''
        save credentials method saves credentials into credentials list
        '''
        Credentials.credentials_list.append(self)


    def delete_credentials(self):
        '''
        delete credentials method removes credentails from the credentials list
        '''
        Credentials.credentials_list.remove(self)


    
    

    




    