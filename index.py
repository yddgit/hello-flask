#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, redirect, url_for, render_template, flash, Blueprint

index_page = Blueprint('index_page', __name__)


@index_page.route("/")
@index_page.route("/index")
def index():
    if 'username' in session:
        return render_template("index.html")
    else:
        flash("You are not logged in!")
        return redirect(url_for("login_page.login"))

