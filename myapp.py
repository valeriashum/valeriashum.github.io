from flask import Flask
from flask import render_template
from flask import request, redirect

import requests

app = Flask(__name__)
email_addresses=[]


@app.route("/")
def hello_world(): 
    return render_template('index.html')

@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails')
def emails():
	return render_template('emails.html', email_addresses = email_addresses)


if __name__ == "__main__":
    app.run()