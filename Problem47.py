def Password (password):
    haveUpper = False
    haveLower = False
    haveNumber = False
    
    if len(password)>=6 and len(password)<=20:
    
        for x in password:
    
            if x.isalpha() == True:
                if x.isupper()==True: 
                    haveUpper =True
                if x.islower()==True:
                    haveLower =True
            elif x.isnumeric()==True:
                #x is not char
                haveNumber=True
        if (haveLower==False):
            print ("password should have at least one lower character")
        if ( haveUpper==False):
               print ("password should have at least one upper character")
        if (haveNumber==False):
            print ("password should have at least one number character")
        if( haveLower and haveNumber and haveUpper )==True:
            print("password is valid")
      
    else:
        print ("password length should be between 6 and 20 characters")
        
    

password=(str(input("enter the password:")))
Password(password)

p=(input("enter to continue......"))