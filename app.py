from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(debug=True)


# pip install Flask
# py app.py
 # https://www.educative.io/edpresso/how-to-add-data-to-databases-in-flask
 # "database search flask"
 # https://www.w3schools.com/css/tryit.asp?filename=trycss_forms
 