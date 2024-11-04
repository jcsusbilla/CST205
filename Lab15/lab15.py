# JC SUSBILLA
# CST205 LAB 15

# hello_flask.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    Hello World
    <p>Student 1: AFK = away from keyboard</p>
    <p>Student 2: BRB = be right back</p>
    """

@app.route('/mytemplate')
def t_test():
   return render_template('my_template_1.html')

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2