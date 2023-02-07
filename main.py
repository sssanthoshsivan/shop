from flask import Flask, flash
from flask import render_template, request
from wtforms.validators import DataRequired
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home", methods=["POST","GET"])
def home():
    name = request.form.get("user")
    info = request.form.get("query")
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True) 