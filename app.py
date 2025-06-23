# API
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def conectar():
    return sqlite3.connect('livros.db')


@app.route('/livros', methods=['GET'])
def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = [
        {"id": row[0], "titulo": row[1], "autor": row[2]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(livros)


@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo = request.get_json()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (titulo, autor) VALUES (?, ?)',
                   (novo['titulo'], novo['autor']))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Livro adicionado com sucesso"}), 201


@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Livro deletado com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)

# To run the application, save this code in a file named app.py and run it using the command:
# python app.py
# You can then access the API at http://
