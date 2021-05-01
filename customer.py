# Emeline JJ - 23858
# Francoise RUCH - 23861

from datetime import date
from pathlib import Path
import os
   
def dictionary(letter):
    chaine = 'abcdefghijklmnopqrstuvwxyz'
    return(1+chaine.index(letter))

def createPin(firstname,lastname):

    initialPositionFirst=dictionary(firstname[0].lower())
    initialPositionLast= dictionary(lastname[0].lower())
    if(initialPositionFirst<10):
        initialPositionFirst=str(0)+str(initialPositionFirst)
    
    if(initialPositionLast<10):
        initialPositionLast=str(0)+str(initialPositionLast)


    pin=str(initialPositionFirst)+str(initialPositionLast)
    return pin

def createAccountNumber(firstname,lastname):

        lenFirst=len(firstname)
        lenLast=len(lastname)       
        
        lenTotal=lenFirst+lenLast

        initialPositionFirst=dictionary(firstname[0].lower())
        initialPositionLast= dictionary(lastname[0].lower())
        if(initialPositionFirst<10):
            initialPositionFirst=str(0)+str(initialPositionFirst)
    
        if(initialPositionLast<10):
            initialPositionLast=str(0)+str(initialPositionLast)

        accountNum=(firstname[0].lower()+lastname[0].lower()+"-"+str(lenTotal)+"-"+str(initialPositionFirst)+"-"+str(initialPositionLast))
        
        return accountNum

def FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount):
        
        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','r')
        filelines = filetransaction.readlines()
        lastline = filelines[ len( filelines )-1]
        lastlinesplit = lastline.split('\t')
        balance = lastlinesplit[3]
        filetransaction.close()
        return balance


class Customer:
    def __init__(self,firstname,lastname,email,pin):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.pin=pin


    
    
    def transaction(firstname,lastname,value,typeOfAccount):
        transfer=False
        dateOfTransaction=date.today().strftime('%d-%m-%Y')
        
        if int(value) <0:
            typeTransaction='Withdrawal'

        else:
            typeTransaction='Lodgement'
        
        nameFile = createPin(firstname,lastname)
        nametxtFile = createAccountNumber(firstname,lastname)
        
        balancesOfAccount= int(FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount)) + int(value)
        if (balancesOfAccount >=0):
            filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','a')
            filetransaction.write('\n'+ dateOfTransaction +'\t'+ typeTransaction +'\t'+ value +'\t'+ str(balancesOfAccount))
            filetransaction.close()
            transfer=True
        

        return transfer
      



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
        
    def deleteCustomer(firstname,lastname):
        delete=False
        
        nameFile = createPin(firstname,lastname)
        nametxtFile = createAccountNumber(firstname,lastname)

        #savings account
        balanceSavings = int(FoundBalanceAccount(nameFile, nametxtFile, 'savings'))
        
        #currents account
        balanceCurrents = int(FoundBalanceAccount(nameFile, nametxtFile, 'currents'))
        
        if (balanceCurrents==0 and balanceSavings==0):
            
            os.remove('Accounts/'+nameFile+'/'+ nametxtFile + '-savings.txt')
            os.remove('Accounts/'+nameFile+'/'+ nametxtFile + '-currents.txt')
            fileToDelete = Path('Accounts/'+nameFile)
            fileToDelete.rmdir()
            delete=True
        
        return delete

    #('Francoise', 'Ruch', 'f@gmail.com')
    #transaction('Francoise', 'Ruch', '500', 'savings')
    print(transaction('Francoise', 'Ruch', '-550', 'savings'))
    deleteCustomer('Francoise','Ruch')
        


    
    


            

    