from flask import Flask, render_template, request
#regular py stuff
import os 
shows = os.listdir('static')

app = Flask(__name__)

@app.route('/'p)
def home():
    return render_template('home.html', shows = shows)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug = True)