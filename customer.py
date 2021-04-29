# Emeline JJ - 23858
# Francoise RUCH - 23861

from datetime import date
   
def dictionary(letter):
    chaine = 'abcdefghijklmnopqrstuvwxyz'
    return(1+chaine.index(letter))

    
class Customer:
    def __init__(self,firstname,lastname,email,pin):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.pin=pin


    def createAccountNumber(firstname,lastname):

        lenFirst=len(firstname)
        lenLast=len(lastname)       
        
        lenTotal=lenFirst+lenLast

        initialPositionFirst=dictionary(firstname[0].lower())
        initialPositionLast= dictionary(lastname[0].lower())
        accountNum=(firstname[0].lower()+lastname[0].lower()+"-"+str(lenTotal)+"-"+str(initialPositionFirst)+"-"+str(initialPositionLast))
        
        return accountNum
    
    def createPin(firstname,lastname):

        initialPositionFirst=dictionary(firstname[0].lower())
        initialPositionLast= dictionary(lastname[0].lower())
        pin=str(initialPositionFirst)+str(initialPositionLast)
        return pin
    
    print(createAccountNumber('Joe', 'Smith'))
    print(createPin('Joe', 'Smith'))
    
    
    def transaction(firstname,lastname,value,typeOfAccount):
        dateOfTransaction=date.today().strftime('%Y-%m-%d')
        
        if value <0:
            typeTransaction='withdraw'
        else:
            typeTransaction='lodgement'
        
        #balancesOfAccount= (balance of old account)- value

        return 'fait'
      

    def FoundBalanceAccount(firstname,lastname,typeOfAccount):
        if typeOfAccount=='savings':
            balance = value #a coder
        else:
            balance = value #a coder

            

    