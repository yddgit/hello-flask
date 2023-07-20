#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, session, redirect, url_for, render_template, flash, Blueprint
from datetime import datetime


login_page = Blueprint("login_page", __name__)


@login_page.get("/login")
@login_page.post("/login")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "password":
            session["username"] = username
            resp = redirect(url_for("index_page.index"))
            resp.set_cookie("login_time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return resp
        else:
            flash("username and password not correct", "error")
            return redirect(url_for("login_page.login"))
    else:
        return render_template("login.html")


@login_page.route("/logout")
def logout():
    session.pop('username', None)
    flash("logout successfully", "success")
    return redirect(url_for("login_page.login"))
