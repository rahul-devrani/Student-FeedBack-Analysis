#Importing Libraries
from flask import Flask, render_template, request, redirect, session
import mysql.connector

# Flask App Setup
app = Flask(__name__)
app.secret_key = 'abc123' 

#Function to Connect to Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rahul", 
        database="feedback_system"
    )

#Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        role = request.form['role']

        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s AND role=%s", (uname, pwd, role))
        data = cur.fetchone()
        con.close()

        if data:
            session['user'] = uname
            session['role'] = role
            if role == 'student':
                return redirect('/feedback')
            else:
                return redirect('/dashboard')
        else:
            return "Wrong username or password"
    return render_template("login.html")

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if session.get('role') != 'student':
        return redirect('/')
    if request.method == 'POST':
        teaching = request.form['teaching']
        content = request.form['content']
        facilities = request.form['facilities']
        suggestion = request.form['suggestion']

        con = connect_db()
        cur = con.cursor()
        cur.execute("INSERT INTO feedback (teaching, content, facilities, suggestion) VALUES (%s, %s, %s, %s)",
                    (teaching, content, facilities, suggestion))
        con.commit()
        con.close()
        return "Thanks for your feedback!"
    return render_template("feedback.html")

@app.route('/dashboard')
def dashboard():
    if session.get('role') != 'admin':
        return redirect('/')

    con = connect_db()
    cur = con.cursor()

    # Get feedback stats
    cur.execute("SELECT COUNT(*), AVG(teaching), AVG(content), AVG(facilities) FROM feedback")
    raw_data = cur.fetchone()

    count = raw_data[0] or 0
    teaching = raw_data[1] or 0
    content = raw_data[2] or 0
    facilities = raw_data[3] or 0

    stats = (count, teaching, content, facilities)

    # Get latest 5 suggestions
    cur.execute("SELECT suggestion FROM feedback ORDER BY id DESC LIMIT 5")
    comments = cur.fetchall()

    con.close()
    return render_template("dashboard.html", stats=stats, suggestions=comments)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
