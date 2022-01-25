from flask import Flask, render_template, request, flash
import sqlite3

DB_PATH = '/app/db/info.db' # only specific to docker container to run

app = Flask(__name__)

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS Monitors(id INETEGER PRIMARY KEY, Title TEXT, Status TEXT, Link TEXT)')
    conn.commit()
    return True

def get_monitors():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT * FROM Monitors')
    results = c.fetchall()

    if results:
        return results
    else:
        return []

def add_monitor(title, link):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT * FROM Monitors WHERE link = ?', (link))

    results = c.fetchall()
    if results: # if it already exists
        return False
    else: # if it doesnt already exist
        c.execute('INSERT INTO Monitors(Title, Link) VALUES(?, ?)', (title, link))
        conn.commit()
        return True

@app.route('/')
def index():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']

        add = add_monitor(title, link)

        if add:
            return render_template('index.html', get_monitors())
        else:
            flash('Invalid Monitor (monitor may already exist)')
            return render_template('index.html', data=get_monitors())
    else:
        return render_template('index.html', data=get_monitors())

if __name__ == '__main__':
    init()
    app.run(debug=True)