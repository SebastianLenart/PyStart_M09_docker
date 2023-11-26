from flask import Flask
from api import authors
from controllers import login, register
app = Flask(__name__)

app.add_url_rule("/authors", view_func=authors.index, methods=["GET"])
app.add_url_rule("/authors", view_func=authors.add, methods=["POST"])
app.add_url_rule("/authors/<author_id>", view_func=authors.delete, methods=["DELETE"])

app.add_url_rule("/login", view_func=login)
app.add_url_rule("/register", view_func=register)





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







































