# Emeline JJ - 23858
# Francoise RUCH - 23861
class Customer:
    def __init__(self,firstname,lastname,email,pin):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.pin=pin

    def createPin(firstname,lastname):
        lenFirst=len(firstname)
        lenLast=len(lastname)

        initialPositionFirst= dictionary(firstname(1))
        initialPositionLast= dictionary(lastname(1))
        pin=lower(firstname(1)+lastname(1)+"-"+lenFirst+"-"+lenFirst+"-"+initialPositionFirst+"-"+initialPositionLast)


    def dictionary(letter):
        chaine = 'abcdefghijklmnopqrstuvwxyz'
        print (1+chaine.index(letter))

    
    