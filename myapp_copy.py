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
    return redirect('/thankyou')

@app.route('/thankyou.html')
	requests.post(
		"https://api.mailgun.net/v3/sandbox16522a5cfadb400b83c6c3c1db813b96.mailgun.org/messages",
        auth=("api", "key-d3df711eb1e752187c7cda1e2520fa78"),
        data={"from": "Judy <judy.shing28@gmail.com>",
              "to": "Customer "<" + email + ">",
               "subject": "Hello for Hall Talk",
               "text": "Congratulations, you just signed up to Hall Talk !"
             }
	)
	return render_template('thankyou.html')

@app.route('/emails')
def emails():
	return render_template('emails.html', email_addresses = email_addresses)


if __name__ == "__main__":
    app.run()