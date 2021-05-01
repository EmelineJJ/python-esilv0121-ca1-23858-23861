# Emeline JJ - 23858
# Francoise RUCH - 23861

from datetime import date
from pathlib import Path
   
def dictionary(letter):
    chaine = 'abcdefghijklmnopqrstuvwxyz'
    return(1+chaine.index(letter))

def createPin(firstname,lastname):

    initialPositionFirst=dictionary(firstname[0].lower())
    initialPositionLast= dictionary(lastname[0].lower())
    pin=str(initialPositionFirst)+str(initialPositionLast)
    return pin

def createAccountNumber(firstname,lastname):

        lenFirst=len(firstname)
        lenLast=len(lastname)       
        
        lenTotal=lenFirst+lenLast

        initialPositionFirst=dictionary(firstname[0].lower())
        initialPositionLast= dictionary(lastname[0].lower())
        accountNum=(firstname[0].lower()+lastname[0].lower()+"-"+str(lenTotal)+"-"+str(initialPositionFirst)+"-"+str(initialPositionLast))
        
        return accountNum

def FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount):
        
        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','r')
        filelines = filetransaction.readlines()
        filetransaction.close()
        lastline = filelines[ len( filelines )-1]
        ligne = lastline.split('\t')
        balance = lastline[3]
        print(balance)
        return balance


class Customer:
    def __init__(self,firstname,lastname,email,pin):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.pin=pin


    print(createAccountNumber('Joe', 'Smith'))
    print(createPin('Joe', 'Smith'))
    
    
    def transaction(firstname,lastname,value,typeOfAccount):
        
        dateOfTransaction=date.today().strftime('%d-%m-%Y')
        
        if int(value) <0:
            typeTransaction='Withdrawal'

        else:
            typeTransaction='Lodgement'
        
        nameFile = createPin(firstname,lastname)
        nametxtFile = createAccountNumber(firstname,lastname)
        balancesOfAccount= int(FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount)) + int(value)

        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','a')
        filetransaction.write('\n'+ dateOfTransaction +'\t'+ typeTransaction +'\t'+ value +'\t'+ str(balancesOfAccount))
        filetransaction.close()
        
        return 'done'
      



    def newCustomer(firstname,lastname,email):
        dateOfCreation =date.today().strftime('%d-%m-%Y')
        nameFile = createPin(firstname,lastname)
        p = Path('Accounts/' + nameFile)
        try:
            p.mkdir()
        except FileExistsError as exc:
            print(exc)
        
        nametxtFile = createAccountNumber(firstname,lastname)
        filesaving = open('Accounts/'+nameFile+'/'+ nametxtFile + '-savings.txt','w')
        filesaving.write(dateOfCreation +'\t' +'Creation'+'\t'+'0'+'\t'+'0')
        filesaving.close()
        filecurrent = open('Accounts/'+nameFile+'/'+ nametxtFile + '-currents.txt','w')
        filecurrent.write(dateOfCreation + '\t' +'Creation'+'\t'+'0'+'\t'+'0')
        filecurrent.close()
        

        
        

    
    newCustomer('Francoise', 'Ruch', 'fr@gmail.com')
    transaction('Francoise', 'Ruch', '50', 'savings')
    transaction('Francoise', 'Ruch', '-50', 'savings')


            

    