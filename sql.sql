CREATE TABLE authors (
id SERIAL PRIMARY KEY,
first_name varchar(255),
last_name varchar(255)
);

INSERT INTO authors(first_name, last_name) VALUES('Jan', 'Kowalski');
INSERT INTO authors(first_name, last_name) VALUES('Ola', 'Pamala');
SELECT * FROM authors;