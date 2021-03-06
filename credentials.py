import random
import string

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
                return credential
            #     return True
            # return False
     
    @classmethod
    def exist(cls,account):
        '''
        method to check if account exists in the list
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False

            
    # def randomPassword (length = 4)  :       
    #     password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
    #     return ''.join(random.choice(password) for i in range(length)) 
    
    def randomPassword (length = 4)  :       
        password = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').lower and ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').upper and ('0,1,2,3,4,5,6,7,8,9') and ('!&$#@*') 
        return ''.join(random.choice(password) for i in range(4))
    




    