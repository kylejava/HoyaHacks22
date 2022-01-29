import requests
from flask import Flask, render_template, flash, request
from Twilio import *
from db import *
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
    name = ""
    phone_number = 0
    astrological_sign = ""
    if(request.method == 'POST'):
        name = request.form['name']
        astrological_sign = request.form.get('astrological_sign')
        phone_number = request.form['phone_number']
        user = User(name, phone_number, astrological_sign)
        addToDatabase(user)
        sendMessage(user)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
