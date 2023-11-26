from flask import Response, request, abort
from db import get_connection
from json import dumps, loads
from psycopg2 import extras
from repositories import AuthorsRepository


def index():
    repository = AuthorsRepository()
    return Response(dumps(repository.get_all()), mimetype="application/json")  # ladniejsza postac jsona


def add():
    repository = AuthorsRepository()
    data = loads(request.data.decode('utf-8'))
    author_id = repository.save(data["first_name"], data["last_name"])
    return Response(dumps({
        "id": author_id
    }), mimetype="application/json", status=201)


def delete(author_id):
    repository = AuthorsRepository()
    author = repository.get()
    if author is None:
        abort(404)
    repository.detele(author_id)
    return Response({
        "status": "ok"
    }, mimetype="application/json", status=200)
