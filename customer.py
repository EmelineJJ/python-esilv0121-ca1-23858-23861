# Emeline JJ - 23858
# Francoise RUCH - 23861
class Customer:
    def __init__(self,firstname,lastname,email,pin):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.pin=pin
   
    def dictionary(letter):
        chaine = 'abcdefghijklmnopqrstuvwxyz'
        return(1+chaine.index(letter))

    

    def createPin(firstname,lastname):

        lenFirst=len(firstname)
        lenLast=len(lastname)       
        
        lenTotal=lenFirst+lenLast

        
        initialPositionFirst=dictionary(firstname[0].lower())
        initialPositionLast= dictionary(lastname[0].lower())
        pin=((firstname[0]+lastname[0])+"-"+lenTotal+"-"+initialPositionFirst+"-"+initialPositionLast).lower()
        return pin
    

    a='Boi'
    b=dictionary(a[0].lower() )
    print(b)

    print(createPin('Joe', 'Smith'))
    
      
    