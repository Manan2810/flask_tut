from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open("config.json","r") as c:
   params=json.load(c)["params"]
   
local_server=True   
app = Flask(__name__)

if (local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(20), nullable=False)
    phone_number=db.Column(db.String(12),nullable=False)
    message=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String,nullable=True)

@app.route('/index')
def home():
    return render_template('index.html',params=params)

@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        # add entry to data base
        
        # data is fetched
        name=request.form.get("name")
        email=request.form.get("email")
        phone_number=request.form.get("phone_number")
        message=request.form.get("message")
        
        entry=Contact(name=name,email=email,phone_number=phone_number,message=message)
        db.session.add(entry)
        db.session.commit()
        
    return render_template('contact.html',params=params)

@app.route('/post')
def post():
    return render_template('post.html',params=params)

if __name__ == '__main__':
    app.run(debug=True)
    
 
