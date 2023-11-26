from flask import render_template


def login():
    return render_template("login.html", hello="Worls", first_name="Kacper")

def register():
    return render_template("register.html")