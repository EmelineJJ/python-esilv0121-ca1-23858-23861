# Francoise RUCH - 23861
# Emeline JJ - 23858

from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class App(db.Model):
    # Doit_on faire un db ?

@app.route("/", methods=["GET","POST"])
def home():
    # To do


@app.route('/employee/<int:id>')
def employee(id):
    #To do
   
@app.route('/customer/<int:id>')
def customer(id):
    #To do

if __name__ == "__main__":
    app.run(debug=True)
