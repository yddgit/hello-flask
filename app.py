#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from flask import make_response
from markupsafe import escape
from markupsafe import Markup
from werkzeug.utils import secure_filename
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Page'


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name, html='<p>html</p>', safe_html='<p style="color:red">SAFE HTML</p>')


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # post_id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show subpath
    return f'Subpath {escape(subpath)}'


# /projects will be redirected to /projects/
@app.route("/projects/")
def projects():
    return "The project page"


# /about/ will produce 404 Not Found
@app.route("/about")
def about():
    return "The about page"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # access form data
        print(request.form)  # form data
        #print(request.form['username'])
        #print(request.form['password'])
        return "do login"
    else:
        print(request.args)  # query string
        print(request.cookies)  # cookie
        resp = make_response("show login form")
        resp.set_cookie("username", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return resp


@app.get("/m/login")
def m_login():
    if not request.args.get('name'):
        abort(401)
    return redirect(url_for("login"))


@app.errorhandler(404)
def not_found(error):
    # 最后一404表示这个页面的HTTP Status Code应该是404，如果不传将会是200
    return render_template('404.html', error=error), 404


@app.get("/get/user")
def get_user():
    return "get user"


@app.post("/post/user")
def post_user():
    return "post user"


@app.route("/upload",  methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('D:/tmp/uploaded_file.txt')
        print(secure_filename(f.filename))
        return 'upload success'
    else:
        return render_template('upload.html')


with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', name='John Doe'))
    print(url_for('show_post', post_id=15))
    print(url_for('show_subpath', subpath='foo/bar'))
    print(url_for('projects'))
    print(url_for('about'))
    print(url_for('static', filename='style.css'))
    print(Markup('<strong> Hello %s!</strong>') % '<blink>hacker</blink>')
    print(Markup.escape('<blink>hacker</blink>'))
    print(Markup('<em>Marked up</em> &raquo; HTML').striptags())


if __name__ == '__main__':
    app.run()
