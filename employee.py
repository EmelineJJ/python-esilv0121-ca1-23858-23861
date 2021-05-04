# Emeline JJ - 23858
# Francoise RUCH - 23861
import re

def FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount):
        
        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','r')
        filelines = filetransaction.readlines()
        lastline = filelines[ len( filelines )-1]
        lastlinesplit = lastline.split('\t')
        balance = lastlinesplit[3]
        filetransaction.close()
        return balance

class Employee:
    def __init__(self,pin):
        self.pin = 'A1234'

    def listofcustomers(withbalances):
        listofallcustomers=[]
        allcustomers= open("Accounts\customers.txt", "r") 
        lines = allcustomers.read().split( )
        customer = 0
       
        if withbalances==True:
            while customer<len(lines):
                line= lines[0+customer]+ lines[1+customer]+ lines[2+customer]+ lines[3+customer]+lines[4+customer]+ str(FoundBalanceAccount(lines[0+customer], lines[3+customer], lines[4+customer])) 
                listofallcustomers.append(line)
                customer= customer+5
        else:
            while customer<len(lines):
                line= lines[0+customer]+ lines[1+customer]+ lines[2+customer]+ lines[3+customer]+lines[4+customer]
                listofallcustomers.append(line)
                customer= customer+5

        return listofallcustomers
    
    print(listofcustomers(True))