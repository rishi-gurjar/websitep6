from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml
import sqlite3

app = Flask(__name__)

#configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app) 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/top')
def top():
    return render_template("top.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/stats', methods = ['GET', 'POST'])
def stats():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template("stats.html")

@app.route('/sports')
def sports():
    return render_template("sports.html")

if __name__ == "__main__":
    app.run(debug=True)


# pip install Flask
# py app.py
# OR FLASK_APP=app.py flask run

# export FLASK_APP=app  
# flask run

# python3 app.py
 # https://www.educative.io/edpresso/how-to-add-data-to-databases-in-flask
 # "database search flask"
 # https://www.w3schools.com/css/tryit.asp?filename=trycss_forms
 