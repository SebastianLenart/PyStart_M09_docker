from flask import Flask
from api import authors
from controllers import login, register, logout, home
from flask_login import LoginManager
from repositories import UserRepository

app = Flask(__name__)
app.config["SECRET_KEY"] = "@@@123@@@"
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    repo = UserRepository()
    return repo.get_by_id(user_id) # musi zwracac obiekt o konkretnych metodach, ale tego dziedziczymy zeby tych funkcji nie tworzyc


app.add_url_rule("/authors", view_func=authors.index, methods=["GET"])
app.add_url_rule("/authors", view_func=authors.add, methods=["POST"])
app.add_url_rule("/authors/<author_id>", view_func=authors.delete, methods=["DELETE"])

app.add_url_rule("/home", view_func=home, methods=["GET"])
app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=logout, methods=["GET"])
app.add_url_rule("/register", view_func=register, methods=["GET", "POST"])

# @app.route("/")
# def hello():
#     return "Hello World"


"""
python3 -m flask run
docker build . w ubuntu trzeba zalogowac sie jako admin czyli suso su
docker-compose up
docker-compose build

python3 -m pytest . # jako admin czyli sudo su i musi byc w tle compose up !!!


http://127.0.0.1:5000/authors
"""
