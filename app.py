import psycopg2
from flask import Flask, request, jsonify, render_template, redirect, url_for
from psycopg2.extras import RealDictCursor

from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/filme', methods=['GET'])
def listar_filme():
    conn = criar_conexao()
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM filmes")
        resposta = cursor.fetchall()
    conn.close()

    return render_template("index.html", filmes=resposta)

@app.route('/filme', methods=['POST'])
def cadastrar_filme():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    campos_obrigatorios = ['usuario_id', 'titulo', 'ano_lancamento', 'genero', 'nota', 'capa_url']
    if not all(campo in dados for campo in campos_obrigatorios):
        return jsonify({"erro": "Dados incompletos"}), 400

    conn = criar_conexao()
    with conn.cursor() as cursor:
        cursor.execute(
            '''
                INSERT INTO filmes (usuario_id, titulo, ano_lancamento, genero, nota, capa_url)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id;
            ''',
            (dados['usuario_id'], dados['titulo'], dados['ano_lancamento'],
             dados['genero'], dados['nota'], dados['capa_url'])
        )
        novo_id = cursor.fetchone()[0]
        conn.commit()
    conn.close()

    return jsonify({
        "message": "Filme salvo com sucesso!",
        "filme-id": novo_id
    }), 201

@app.route('/deletar/<int:id>', methods=["POST"])
def deletar_filme(id):
    conn = criar_conexao()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM filmes WHERE id = %s", (id,))
        conn.commit()
    conn.close()

    return redirect(url_for("listar_filme"))

@app.route('/novo', methods=["GET", "POST"])
def novo_filme():
    if request.method == "POST":
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        capa_url = request.form["capa"]
        nota = request.form["nota"]
        ano_lancamento = request.form["ano_lancamento"]
        usuario_id = 1

        parametros = [titulo, genero, capa_url, nota, ano_lancamento, usuario_id]
        sql = '''
            INSERT INTO filmes
            (titulo, genero, capa_url, nota, ano_lancamento, usuario_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        conn = criar_conexao()
        with conn.cursor() as cursor:
            cursor.execute(sql, parametros)
            conn.commit()
        conn.close()
        return redirect(url_for("listar_filme"))

    return render_template("novo_filme.html")

@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    conn.close()
    return jsonify({"message": "banco conectado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)