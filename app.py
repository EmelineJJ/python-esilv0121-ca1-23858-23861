# Francoise RUCH - 23861
# Emeline JJ - 23858
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

        path = 'Accounts/customers.txt'
        # Vérifier si le chemin existe ou non
        if os.path.exists(path) :
            filecustomer = open('Accounts/customers.txt','a')
            filecustomer.write('\n'+ nameFile + '\t' +nametxtFile+'\t'+'savings')
            filecustomer.write('\n'+nameFile + '\t' +nametxtFile+'\t'+'currents')
        else:
            filecustomer = open('Accounts/customers.txt','a')
            filecustomer.write(nameFile + '\t' +nametxtFile+'\t'+'savings')
            filecustomer.write('\n'+nameFile + '\t' +nametxtFile+'\t'+'currents')
        
        filecustomer.close()
        
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
            deleteLine(nameFile)
           
            delete=True
        
        return delete

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
    err = None
    if request.method == 'POST' :
        if request.form['password'] != 'A1234':
            err = 'Invalid Password. Please try again.'
        else:
            return render_template("appEmployee.html")
    return render_template("loginEmployee.html", error=err)


@app.route('/customer/app', methods=["POST"])
def appCustomer():

    entries = os.listdir('Accounts/')
    print(entries)
    exist=False
    pin=request.form['pin']
    for i in range(len(entries)):
        if entries[i] == pin :
            exist = True

    if exist == True:
        return render_template("appCustomer.html")
    else :
        return 'Try again !'

@app.route('/employee/app/create',methods=["POST"])
def createCustomer():
    firstna = request.form['createfirstname']
    lastna = request.form['createlastname']
    email = request.form['email']
    if request.method =="POST":
        Customer.newCustomer(firstna,lastna,email)
    return render_template("appEmployee.html", error= 'Customer created')

@app.route('/employee/app/delete',methods=["POST"])
def deleteCustomer():
    firstna = request.form['deletefirstname']
    lastna = request.form['deletelastname']

    if request.method =="POST":
        
        result = Customer.deleteCustomer(firstna,lastna)
        if result == False:
            return render_template("appEmployee.html", error= 'The customer need to have 0 balances')
        else :
            return render_template("appEmployee.html", error= 'Customer deleted')

    

@app.route('/employee/app/transaction',methods=["POST"])
def transactionEmployee():
    firstna = request.form['transactionfirstname']
    lastna = request.form['transactionlastname']
    value = request.form['valuetransaction']
    typeOfAccount = request.form['actype']
    if request.method =="POST":
        result = Customer.transaction(firstna, lastna, value, typeOfAccount)
        if result == False:
            return render_template("appEmployee.html", error= 'Impossible transaction')
        else :
            return render_template("appEmployee.html", error= 'Transaction done')

@app.route('/customer/app/transaction',methods=["POST"])
def transactionCustomer():
    firstna = request.form['transactionfirstname']
    lastna = request.form['transactionlastname']
    value = request.form['valuetransaction']
    typeOfAccount = request.form['actype']
    if request.method =="POST":
        result = Customer.transaction(firstna, lastna, value, typeOfAccount)
        if result == False:
            return render_template("appCustomer.html", error= 'Impossible transaction ')
        else :
            return render_template("appCustomer.html", error= 'Transaction done')


if __name__ == "__main__":
    app.run(debug=True)
