# Emeline JJ - 23858
# Francoise RUCH - 23861

from datetime import date
from pathlib import Path
import os

#region Abstract Class : Users
from abc import ABC # For abstract class
class Users(ABC):
    def __init__(self,pin):
        self.pin = pin
#endregion


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

def createAccountNumber(cust):

        lenFirst=len(cust.firstname)
        lenLast=len(cust.lastname)       
        
        lenTotal=lenFirst+lenLast

        initialPositionFirst=dictionary(cust.firstname[0].lower())
        initialPositionLast= dictionary(cust.lastname[0].lower())
        if(initialPositionFirst<10):
            initialPositionFirst=str(0)+str(initialPositionFirst)
    
        if(initialPositionLast<10):
            initialPositionLast=str(0)+str(initialPositionLast)

        accountNum=(cust.firstname[0].lower()+cust.lastname[0].lower()+"-"+str(lenTotal)+"-"+str(initialPositionFirst)+"-"+str(initialPositionLast))
        
        return accountNum

def FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount):
        
        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeOfAccount+'.txt','r')
        filelines = filetransaction.readlines()
        lastline = filelines[ len( filelines )-1]
        lastlinesplit = lastline.split('\t')
        balance = lastlinesplit[3]
        filetransaction.close()
        return balance

def deleteLine(deletePin):
    fn = 'Accounts/customers.txt'
    f = open(fn)
    output = []
    str=deletePin
    for line in f:
        if not line.startswith(str):
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

def replaceLine(nameFile,typeOfAccount,newString):
    fn = 'Accounts/customers.txt'
    f = open(fn)
    lines = f.readlines()
    output = []
    for line in lines:
        if (line.find(nameFile)!=-1 )and (line.find(typeOfAccount)!=-1):
            output.append(newString)   
        else:
            output.append(line)  
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

#region Inheritance Class : Customers
class Customer(Users):
    def __init__(self,pin,firstname,lastname,email):
        Users.__init__(self,pin)
        self.pin = pin
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
       
    #region Transaction
    def transaction(self,value,typeOfAccount):
        transfer=False
        dateOfTransaction=date.today().strftime('%d-%m-%Y')
        
        if int(value) <0:
            typeTransaction='Withdrawal'

        else:
            typeTransaction='Lodgement'
        
        nameFile = createPin(self.firstname,self.lastname)
        nametxtFile = createAccountNumber(self)
        
        oldBalance=int(FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount)) 
        newBalance= int(FoundBalanceAccount(nameFile,nametxtFile,typeOfAccount)) + int(value)
        if (newBalance >=0):
            filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile +'-'+typeOfAccount+'.txt','a')
            filetransaction.write('\n'+ dateOfTransaction +'\t'+ typeTransaction +'\t'+value+'\t'+str(newBalance))
            filetransaction.close()

            newString = nameFile+'\t'+ self.firstname+'\t'+ self.lastname+'\t'+ nametxtFile+ '\t'+ typeOfAccount+'\t'+ str(newBalance)+'\n'
            
            replaceLine(nameFile,typeOfAccount,newString)
            
            transfer=True
        return transfer
    
    
    #endregion  

    #region Create new customer
    def newCustomer(self):   
        dateOfCreation =date.today().strftime('%d-%m-%Y')
        nameFile = createPin(self.firstname,self.lastname)
        p = Path('Accounts/'+nameFile)
        try:
            p.mkdir()
            nametxtFile = createAccountNumber(self)
            filesaving = open('Accounts/'+nameFile+'/'+ nametxtFile + '-savings.txt','w')
            filesaving.write(dateOfCreation+'\t'+'Creation'+'\t'+'0'+'\t'+'0')
            filesaving.close()
        
            filecurrent = open('Accounts/'+nameFile+'/'+nametxtFile+'-currents.txt','w')
            filecurrent.write(dateOfCreation+'\t'+'Creation'+'\t'+'0'+'\t'+'0')
            filecurrent.close()

            path = 'Accounts/customers.txt'
        
            if os.path.exists(path) :
                filecustomer = open('Accounts/customers.txt','a')
                filecustomer.write('\n'+nameFile +'\t'+ self.firstname +'\t'+self.lastname+'\t'+nametxtFile+'\t'+'savings'+'\t'+'0')
                filecustomer.write('\n'+nameFile +'\t'+ self.firstname +'\t'+self.lastname+'\t'+nametxtFile+'\t'+'currents'+'\t'+'0')
                
            else:
                filecustomer = open('Accounts/customers.txt','w')
                filecustomer.write(nameFile +'\t'+ self.firstname +'\t'+self.lastname+'\t'+nametxtFile+'\t'+'savings'+'\t'+'0')
                filecustomer.write('\n'+nameFile +'\t'+ self.firstname+'\t'+self.lastname+'\t'+nametxtFile+'\t'+'currents'+'\t'+'0')
        
            filecustomer.close()
        except FileExistsError as exc:
            print(exc)
        
        
    #endregion
 
    #region Delete a customer
    def deleteCustomer(self):
        delete=False 
        nameFile = createPin(self.firstname,self.lastname)
        nametxtFile = createAccountNumber(self)

        #savings account
        balanceSavings = int(FoundBalanceAccount(nameFile, nametxtFile, 'savings'))
        
        #currents account
        balanceCurrents = int(FoundBalanceAccount(nameFile, nametxtFile, 'currents'))
        
        if (balanceCurrents==0 and balanceSavings==0):  
            os.remove('Accounts/'+nameFile+'/'+ nametxtFile + '-savings.txt')
            os.remove('Accounts/'+nameFile+'/'+ nametxtFile + '-currents.txt')
            fileToDelete = Path('Accounts/'+nameFile)
            fileToDelete.rmdir()
            deleteLine(nameFile)
            delete=True
        
        return delete
    #endregion

    #region transaction
    def listofTransaction(self,typeAccount):
        listoftransaction=[]
        nameFile = createPin(self.firstname,self.lastname)
        nametxtFile = createAccountNumber(self)
        filetransaction = open('Accounts/'+nameFile+'/'+ nametxtFile + '-'+typeAccount+'.txt','r') 
        lines = filetransaction.read().split('\n')
        
        for line in lines:
            listoftransaction.append(line)
        
        return  listoftransaction
    
    #endregion
#endregion



#region Test

p ='0000'
j= Customer(p,'Jules', 'Joe', 'j@gmail.com')
Customer.newCustomer(j)
    
e= Customer(p,'Emeline', 'Jacques', 'e@gmail.com')
Customer.newCustomer(e)
    
f= Customer(p,'Francoise', 'Ruch', 'f@gmail.com')
Customer.newCustomer(f)
    
Customer.transaction(e, '500', 'savings')
Customer.transaction(e, '500', 'currents')

Customer.transaction(f, '200', 'savings')
Customer.transaction(f, '10', 'currents')

#endregion

#region Inheritance Class: Employee
class Employee(Users):
    def __init__(self,pin):
        Users.__init__(self, pin)
        self.pin = 'A1234'
    #region List of customers and their balances
    def listofcustomers():
        listofallcustomers=[]
        allcustomers= open("Accounts\customers.txt", "r") 
        lines = allcustomers.read().split('\n')
        allcustomers.close()
        return lines

    #endregion
#endregion

#region App for HTML
from flask import Flask, render_template,request
import os

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")


@app.route('/employee')
def employee():
     return render_template("loginEmployee.html", id = 'A1234')
   
@app.route('/customer')
def customer():
     return render_template("loginCustomer.html")

@app.route('/employee/app', methods=["POST"])
def appEmployee():
    if request.method == 'POST' :
        if request.form['password'] != 'A1234':
            return render_template("loginEmployee.html", error='Invalid Password. Please try again.')
        else:
            return render_template("appEmployee.html", key=Employee.listofcustomers())
    


@app.route('/customer/app', methods=["POST"])
def appCustomer():
    entries = os.listdir('Accounts/')
    exist=False
    for i in range(len(entries)):
        if entries[i] == request.form['pin'] :
            exist = True

    if exist == False:
        return render_template("loginCustomer.html", error = 'Try again')
    else : 
        return render_template("appCustomer.html")

@app.route('/customer/app/history', methods=["POST"])
def hitoryOfAccounts():
    firstna = request.form['listfirstname']
    lastna = request.form['listlastname']
    email = request.form['listemail']
    typeOfAccounts = request.form['actype2']
    if request.method =="POST":
        cust = Customer('0000',firstna,lastna,email)
        listHistory = Customer.listofTransaction(cust,typeOfAccounts)
    return render_template("appCustomer.html",key = listHistory)

@app.route('/employee/app/create',methods=["POST"])
def createCustomer():
    firstna = request.form['createfirstname']
    lastna = request.form['createlastname']
    email = request.form['email']
    if request.method =="POST":
        new = Customer('0000',firstna,lastna,email)
        Customer.newCustomer(new)
    return render_template("appEmployee.html", error1= 'Customer created')

@app.route('/employee/app/delete',methods=["POST"])
def deleteCustomer():
    firstna = request.form['deletefirstname']
    lastna = request.form['deletelastname']
    email =  request.form['deleteemail']
    if request.method =="POST":
        toDelete = Customer('0000',firstna,lastna, email)
        result = Customer.deleteCustomer(toDelete)
        if result == False:
            return render_template("appEmployee.html", error2= 'The customer need to have 0 balances')
        else :
            return render_template("appEmployee.html", error2= 'Customer deleted')

    

@app.route('/employee/app/transaction',methods=["POST"])
def transactionEmployee():
    firstna = request.form['transactionfirstname']
    lastna = request.form['transactionlastname']
    email =  request.form['transactionemail']
    value = request.form['valuetransaction']
    typeOfAccount = request.form['actype']
    if request.method =="POST":
        custom = Customer('0000',firstna, lastna, email)
        result = Customer.transaction(custom, value, typeOfAccount)
        if result == False:
            return render_template("appEmployee.html", error3= 'Impossible transaction')
        else :
            return render_template("appEmployee.html", error3= 'Transaction done')

@app.route('/customer/app/transaction',methods=["POST"])
def transactionCustomer():
    firstna = request.form['transactionfirstname']
    lastna = request.form['transactionlastname']
    email =  request.form['transactionemail']
    value = request.form['valuetransaction']
    typeOfAccount = request.form['actype']
    if request.method =="POST":
        custom = Customer('0000',firstna, lastna, email)
        result = Customer.transaction(custom, value, typeOfAccount)
        if result == False:
            return render_template("appCustomer.html", error= 'Impossible transaction ')
        else :
            return render_template("appCustomer.html", error= 'Transaction done')


if __name__ == "__main__":
    app.run(debug=True)

#endregion  