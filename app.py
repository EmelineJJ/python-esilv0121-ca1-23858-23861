# Francoise RUCH - 23861
# Emeline JJ - 23858

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

if __name__ == "__main__":
    app.run(debug=True)

