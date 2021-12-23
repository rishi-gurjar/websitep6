from flask import Flask, render_template, request, request, jsonify
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
db = MySQLdb.connect(host= "localhost", user="root", passwd="Samahita0")
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Samahita0'
app.config['MYSQL_DB'] = 'testingdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
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

@app.route('/stats')
def stats():
    return render_template("stats.html")

@app.route('/sports')
def sports():
    return render_template("sports.html")

@app.route("/searchdata",methods=["POST","GET"])
def searchdata():
    if request.method == 'POST':
        search_word = request.form['search_word']
        print(search_word)
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * from LeagueSearch WHERE League LIKE '%{}%' ORDER BY id DESC LIMIT 20".format(search_word)
        cur.execute(query)
        programming = cur.fetchall()
    return jsonify({'data': render_template('response.html', programming=programming)})

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')



# pip install Flask

# py app.py
# OR FLASK_APP=app.py flask run

# export FLASK_APP=app  

# flask run
