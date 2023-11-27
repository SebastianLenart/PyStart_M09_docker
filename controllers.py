from flask import render_template, request
from forms import RegisterForm, LoginForm
from repositories import UserRepository
from hashlib import pbkdf2_hmac


def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user_name = form.username.data
        crypted_password = crypt_password(form.password.data)
        repository = UserRepository()
        user = repository.get_by_name(user_name)
        print(user["password"], "\n", crypted_password)
    print("ASASASASs")
    return render_template("login.html", hello="Worls", form=form)




def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():  # kolejnosc ma znaczenie, najpierw wysyla potem validuje wiec poprawki sie nie pojawiaja od razu
        # 1. hash password
        # 2. create repository
        # 3. user save method on repository
        user_name = form.username.data
        password = crypt_password(form.password.data)
        repository = UserRepository()
        repository.save(user_name, password)

    return render_template("register.html", form=form)


def crypt_password(password):
    salt = "qwerty321"
    password = pbkdf2_hmac("sha256", password.encode("utf-8"), salt=salt.encode("utf-8"), iterations=999)
    return password.hex()
