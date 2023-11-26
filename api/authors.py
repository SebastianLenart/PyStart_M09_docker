from flask import Response, request, abort
from json import dumps, loads
from repositories import AuthorsRepository
from models import Author
from pydantic import ValidationError


def index():
    repository = AuthorsRepository()
    return Response(dumps(repository.get_all()), mimetype="application/json")  # ladniejsza postac jsona


def add():
    repository = AuthorsRepository()
    data = loads(request.data.decode('utf-8'))
    try:
        # walidacja
        author = Author(**data)
        author_id = repository.save(author.first_name, author.last_name)
        return Response(dumps({
            "id": author_id
        }), mimetype="application/json", status=201)
    except ValidationError as error: # nie podales first name i/lub lastname
        return Response(error.json(), mimetype="application/json", status=400)




def delete(author_id):
    repository = AuthorsRepository()
    author = repository.get()
    if author is None:
        abort(404)
    repository.detele(author_id)
    return Response({
        "status": "ok"
    }, mimetype="application/json", status=200)
