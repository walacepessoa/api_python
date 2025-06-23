# API
from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
    },
    {
        "id": 2,
        "titulo": "1984",
        "autor": "George Orwell",
    },
    {
        "id": 3,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
    }
]
@app.route('/livros', methods=['GET'])


def get_livros():
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
