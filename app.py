from flask import Flask, render_template, request

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

# Database connection info. Note that this is not a secure connection.
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
#app.config['MYSQL_DATABASE_DB'] = 'LibraryDB'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#mysql = MySQL()
#mysql.init_app(app)
#conn = mysql.connect()
#cursor = conn.cursor()

#endpoint for search
#@app.route('/search', methods=['GET', 'POST'])
#def search():
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT name, author from Book WHERE name LIKE %s OR author LIKE %s", (book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all': 
            cursor.execute("SELECT name, author from Book")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')


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
 