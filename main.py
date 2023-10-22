import flask
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort

def get_con():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
app = Flask(__name__)

def det_post(post_id):
    conn = get_con()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post
                            
@app.route('/')
def index():
    conn = get_con()
    post = conn.execute().fetchall()
    conn.close()
    return render_template('index.html', posts = post)

@app.route('/new_page')
def new_page():
    return "New page"

@app.route('/pipapu')
def pipapu():
    return "Pipapu-pipapu"

@app.route('/hi')
def hi():
    return "my name is Gustav"

@app.route('/pam_pam_ram')
def pam_pam_ram():
    return "para ram pam pam"

app.run()
