from flask import Flask
from flask import render_template
from flask import request, redirect

import requests

app = Flask(__name__)
email_addresses=[]


@app.route("/")
def hello_world(): 
    return render_template('index.html')

@app.route("/index.html")
def hello_world1(): 
    return render_template('index.html')
    
@app.route("/climate_change.html")
def hello_world2(): 
    return render_template('climate_change.html')
    
@app.route("/podcasts.html")
def hello_world3(): 
    return render_template('podcasts.html')
    
@app.route("/refugee_crisis.html")
def hello_world4(): 
    return render_template('refugee_crisis.html')
    
@app.route("/blog-post.html")
def hello_world5(): 
    return render_template('blog-post.html')
    
@app.route("/blog-post1.html")
def hello_world6(): 
    return render_template('blog-post1.html')
    
@app.route("/blog-post2.html")
def hello_world7(): 
    return render_template('blog-post2.html')

@app.route("/blog.html")
def hello_world10(): 
    return render_template('blog.html')

@app.route("/portfolio.html")
def hello_world8(): 
    return render_template('portfolio.html')
    
@app.route("/videos.html")
def hello_world9(): 
    return render_template('videos.html')
    
@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
	
	return render_template('thankyou.html')

@app.route('/emails')
def emails():
	return render_template('emails.html', email_addresses = email_addresses)


if __name__ == "__main__":
    app.run()