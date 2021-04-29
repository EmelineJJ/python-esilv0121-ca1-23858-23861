# Francoise RUCH - 23861
# Emeline JJ - 23858

from flask import Flask, render_template,request

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
    id = 'A1234'
    password=request.form['password']

    if password == id :
        return render_template("appEmployee.html")
    else:
        return "Try again !"

if __name__ == "__main__":
    app.run(debug=True)
