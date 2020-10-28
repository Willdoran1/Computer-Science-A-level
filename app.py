from flask import Flask, render_template 


app = Flask(__name__)


@app.route('/index')
def index():
    user= 'will'


    return render_template('index.html',user=user)
