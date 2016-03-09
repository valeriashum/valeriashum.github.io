from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask(__name__)

f = open('data.txt', 'w')

@app.route("/")
def hello(): 
	return render_template("index.html")

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	#print form_data['name']
	#print form_data ['email']
	f.write('%s \n' % (form_data['email']))
	#name = form_data['name']
	#email = form_data['email']

	#requests.post(
		# "https://api.mailgun.net/v3/sandbox16522a5cfadb400b83c6c3c1db813b96.mailgun.org/messages",
  #       auth=("api", "key-d3df711eb1e752187c7cda1e2520fa78"),
  #       data={"from": "Judy <judy.shing28@gmail.com>",
  #             "to": name + "<" + email + ">",
  #             "subject": "Hello " + name,
  #             "text": "Congratulations " + name + ", you just signed up!"
  #           }
		# 	)
	return "all ok"
	# return render_template("hello.html", name=name.title())

app.run(debug=True)