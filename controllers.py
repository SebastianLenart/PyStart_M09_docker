from flask import render_template, request,abort, redirect
from forms import RegisterForm, LoginForm
from repositories import UserRepository
from hashlib import pbkdf2_hmac
from flask_login import login_user, logout_user, login_required

def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user_name = form.username.data
        crypted_password = crypt_password(form.password.data)
        repository = UserRepository()
        user = repository.get_by_name(user_name)
        # print(user.password, "\n", crypted_password)
        if user.password == crypted_password:
            login_user(user)
            return redirect("/home")
        else:
            abort(400)
    return render_template("login.html", hello="Worls", form=form)

def logout():
    logout_user()
    return redirect("/login")

@login_required # tylko dla zalogowanych, ale jak flask wie ze jestem zalogfowanyc ? cache ciastka? bufor jakis ?
def home():
    return render_template("home.html")


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
