import requests


def test_fet_authors():
    response = requests.get("http://localhost:5000/authors")
    assert response.status_code == 200

# czy po dodaniu autora mam o 1 autora wiecej

# def test_add_author():
#     # given
#     payload = {
#         "first_name": "Grzegosz",
#         "last_name": "Lenart"
#     }
#     # when
#     response = requests.post("http://localhost:5000/authors", payload)
#
#     # then
#     assert response == 201
#
#     response = requests.get("http://localhost:5000/authors")
#     data = response.json()
#     assert data[-1].first_name == "Grzegorz"
#
# def test_delete_author():
#     resposne = requests.get("http://localhost:5000/authors")
#     data = resposne.json()
#     quantity = len(data)
#     last_id = data[-1].id
#     requests.delete(f"http://localhost:5000/authors/{last_id}")
#     resposne = requests.get("http://localhost:5000/authors")
#     data = resposne.json()
#     new_quantity = len(data)
#     assert new_quantity + 1 == quantity





















