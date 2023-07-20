#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, redirect, url_for, request, render_template
from markupsafe import escape, Markup
from werkzeug.utils import secure_filename

from index import index_page
from login import login_page

app = Flask(__name__)


# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = b'17b753b771fc89b6128e590a009c06a2fbb0be37992841860d6452ac2f80b9fa'
app.register_blueprint(index_page)
app.register_blueprint(login_page)

# @app.route("/")
# def index():
#     return 'Index Page'


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


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         # access form data
#         print(request.form)  # form data
#         #print(request.form['username'])
#         #print(request.form['password'])
#         return "do login"
#     else:
#         print(request.args)  # query string
#         print(request.cookies)  # cookie
#         resp = make_response("show login form")
#         resp.set_cookie("username", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         return resp


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


@app.get("/me")
def me_api():
    return {
        "name": "yang",
        "birthday": "1997-01-01",
        "image": "https://www.example.com/avatar.png"
    }


@app.get("/users")
def users_api():
    return [
        {
            "name": "yang",
            "birthday": "1997-01-01",
            "image": "https://www.example.com/avatar_yang.png"
        },
        {
            "name": "qian",
            "birthday": "1997-02-01",
            "image": "https://www.example.com/avatar_qian.png"
        }
    ]


with app.test_request_context():
    app.logger.debug(url_for('index_page.index'))
    app.logger.info(url_for('hello'))
    app.logger.warning(url_for('hello', name='John Doe'))
    app.logger.error(url_for('show_post', post_id=15))
    app.logger.debug(url_for('show_subpath', subpath='foo/bar'))
    app.logger.info(url_for('projects'))
    app.logger.warning(url_for('about'))
    app.logger.error(url_for('static', filename='style.css'))
    app.logger.debug(Markup('<strong> Hello %s!</strong>') % '<blink>hacker</blink>')
    app.logger.info(Markup.escape('<blink>hacker</blink>'))
    app.logger.warning(Markup('<em>Marked up</em> &raquo; HTML').striptags())


if __name__ == '__main__':
    app.run()
