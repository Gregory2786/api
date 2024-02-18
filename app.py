from flask import Flask, jsonify, request

app = Flask(__name__)

pessoas = [

    {
       'id': 1,
       'nome': 'Maria', 
    },
    
    {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    },

]

#visualizar todas as pessoas
@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    return jsonify(pessoas)

#Consultar por Id
@app.route('/pessoas/<int:id>', methods=['GET'])
def obter_pessoas_por_id(id):
    for pessoa in pessoas:
       if pessoa.get('id') == id:
           return jsonify( pessoa)

#Editar
@app.route('/pessoas/<int:id>', methods=['PUT'])
def editar_pessoa_por_id(id):
   pessoa_alterada = request.get_json()
   for indice,pessoa in enumerate(pessoas):
      if pessoa.get(id) == id:
          pessoas[indice].update(pessoa_alterada)
          return jsonify(pessoas[indice])

#Criar
@app.route('/pessoas', methods=['POST'])
def incluir_nova_pessoa():
    nova_pessoa = request.get_json()
    pessoas.append(nova_pessoa)
    return jsonify(pessoas)

#Excluir
@app.route('\pessoas/int:id', methods=['DELETE'])
def excluir_pessoas(id):
    for indice, livro in enumerate(pessoas):
        if livro.get('id') == id:
            del pessoas[indice]
            
            return jsonify(pessoas)
        





















app.run(port=5000,host='localhost',debug=True)