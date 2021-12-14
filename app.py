from flask import Flask
import random
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    print(rows)
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    
    cursor.execute("SELECT * FROM topics WHERE id = ?", (id, ))
    topic = cursor.fetchall()
    return f"""
    <html>
    <body>
        <h1><a href="/index.html">web</a></h1>
        <ul>
            {liTag}
        </ul>
        <h2>Welcome</h2>
        Hello, WEB
    </body>
    </html>
    """

@app.route("/read/<id>/", defaults={'username': None})
@app.route("/read/<id>/")
def read(id):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    print(rows)
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    
    cursor.execute("SELECT * FROM topics WHERE id = ?", (id, ))
    topic = cursor.fetchall()
    return f"""
    <html>
    <body>
        <h1><a href="/index.html">web</a></h1>
        <ul>
            {liTag}
        </ul>
        <h2>Welcome</h2>
        Hello, WEB
    </body>
    </html>
    """


@app.route("/create/<id>/")
def create(id):
    return "create"+id

app.run(debug=True,host='0.0.0.0',port='8000')