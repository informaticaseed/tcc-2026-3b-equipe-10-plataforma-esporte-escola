from flask import Flask, jsonify, request

from banco import criar_banco
import repositorio


app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "API Esporte Escolar funcionando!"
    })


@app.route("/escolas", methods=["GET"])
def escolas():
    return jsonify(repositorio.listar_escolas())


@app.route("/escolas", methods=["POST"])
def cadastrar_escola():
    dados = request.json

    if not dados:
        return jsonify({
            "erro": "Dados não enviados"
        }), 400

    nome = dados.get("nome")
    endereco = dados.get("endereco")
    telefone = dados.get("telefone")

    if not nome:
        return jsonify({
            "erro": "O nome da escola é obrigatório"
        }), 400

    repositorio.cadastrar_escola(
        nome,
        endereco,
        telefone
    )

    return jsonify({
        "mensagem": "Escola cadastrada com sucesso!"
    }), 201


@app.route("/esportes", methods=["GET"])
def esportes():
    return jsonify(repositorio.listar_esportes())


@app.route("/atividades", methods=["GET"])
def atividades():
    return jsonify(repositorio.listar_atividades())


@app.route("/atividades", methods=["POST"])
def cadastrar_atividade():
    dados = request.json

    campos = [
        "escola_id",
        "esporte_id",
        "dia_semana",
        "horario",
        "local"
    ]

    for campo in campos:
        if campo not in dados:
            return jsonify({
                "erro": f"O campo '{campo}' é obrigatório"
            }), 400

    repositorio.cadastrar_atividade(
        dados["escola_id"],
        dados["esporte_id"],
        dados["dia_semana"],
        dados["horario"],
        dados["local"]
    )

    return jsonify({
        "mensagem": "Atividade cadastrada com sucesso!"
    }), 201


if __name__ == "__main__":
    criar_banco()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
  )
