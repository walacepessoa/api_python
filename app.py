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


@app.route('/livros', methods=['GET'])
def consultar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({"error": "Livro não encontrado"}), 404


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        dados = request.get_json()
        livro.update(dados)
        return jsonify(livro)
    return jsonify({"error": "Livro não encontrado"}), 404


@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    global livros
    livros = [livro for livro in livros if livro['id'] != id]
    return jsonify({"message": "Livro excluído com sucesso"}), 204


app.run(port=5000, host='localhost', debug=True)
