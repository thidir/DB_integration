from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

def connect_to_db() -> sqlite3.Connection:
    conn = sqlite3.connect("main.db")
    return conn




@app.get('/')
def homepage()-> str:
    
    return render_template("index.html")

@app.get('/submit')
@app.post('/submit')
def submit_data():
    if request.method == 'POST':
        Firstname = request.form['firstname']
        Lastname = request.form['lastname']
        email = request.form['email']

        try:
            con = connect_to_db()
            con.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY AUTOINCREMENT
                Firstname TEXT NOT NULL,
                Lastname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )    
            ''')
            con.execute('''INSERT INTO users
                        (Firstname,
                        Lastname,email)
                        VALUES(
                        ?,?,?)
            ''',(Firstname,Lastname,email))
            con.commit()
            con.close()
            return "successful"
        except sqlite3.Error as e:
            return str(e)   
        
    return render_template("index.html")


    
    

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")


