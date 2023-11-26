from flask import Response, request, abort
from db import get_connection
from json import dumps, loads
from psycopg2 import extras

class AuthorsRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def get_all(self):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors')
        return self.cursor.fetchall()

    def save(self, first_name, last_name):
        self.cursor.execute('INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING id',
                            (first_name, last_name))
        author_id = self.cursor.fetchone()[0]
        self.connection.commit()
        return author_id

    def get(self, author_id):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors WHERE id = %s', (author_id,))
        return self.cursor.fetchone()

    def delete(self, author_id):
        self.cursor.execute("DELETE FROM authors WHERE id = %s", (author_id,))
        self.connection.commit()