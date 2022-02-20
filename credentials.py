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


    @classmethod
    def display_credentials(cls):
        '''
        display the creadentials in the credentials list
        '''
        return cls.credentials_list

    
    @classmethod
    def find_credentials(cls,account):
        '''
        method finds the credentials depending on the account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False
        


    
    

    




    