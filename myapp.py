from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world(): 
    return render_template('index.html')

@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    f=open('emails.txt','w')
    print("This email address is ' " + email + "'", f)
    return redirect('/')

if __name__ == "__main__":
    app.run()