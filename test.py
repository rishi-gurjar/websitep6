import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Samahita0",
    database = "testdb"
)

mycursor = db.cursor()

#--------
#mycursor.execute("CREATE TABLE User (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO User (name, age) VALUES (%s, %s)", ("Joe", 22))
#db.commit() #Commit Changes to Database
#mycursor.execute("SELECT * FROM User")
#for x in mycursor:
#    print(x)
#--------

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Martha", datetime.now(), "F"))



print("works yay")