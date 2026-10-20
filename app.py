from flask import Flask, request, jsonify

from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario ={
        "nome": "Sophia",
        "idade": 16,
        "telefone": "(19) 9967676767"
    }
    return usuario


@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f"Novo produto: {dados}")

    return jsonify(
        {
            "message": "Produto salvo com sucesso!",
            "produto-cadastrado": dados
        }
    ), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
    "id": 1,
    "nome": "lápis preto",
    "preco": 1.5,
    "quantidade": 20,
    "descricao": "Lápis preto com borracha",
    "marca": "Faber Castell"
}
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados['id'] == produto['id']:
        produto = dados

        print(f'Produto atualizado: {produto}')

        return jsonify({"message": "Produto atualizado com sucesso!"}), 201
    else:
        return jsonify({"message": "Produto não encontrado"}), 400


@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Testando conexão: ', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso!"}), 200




if __name__ == "__main__":
    app.run(debug=True)