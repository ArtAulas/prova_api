from flask import Flask , request
import model_cep

'''
Modelo 4
Q1: Rota de inserir e consulta por id
Q2: Rota de exclusão
Q3: Rota de pesquisa
Q4: Cod de status para not found
Q5: rota de edição
'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'Tente tb a url /ola'

@app.route('/ola')
def bom_dia():
    return 'olá, bom dia'

@app.route('/cep/todos',methods=['GET'])
def rota_todos():
    return model_cep.todos()

#Resolução da Q1
#Exemplo dicionário válido= {'CEP':'27251165','endereco':'Rua C','estado':'RJ','cidade':'Volta Redonda'}
@app.route('/cep/adiciona',methods=['POST'])
def rota_adiciona():
    try:
        dici=request.json
        model_cep.adiciona(dici)
        return 'endereco adicionado'
    except model_cep.JaCadastradoError:
        return {'erro':'cep ja cadastrado'},400

@app.route('/cep/<int:id>',methods=['GET'])
def rota_consulta_id(id):
    try:
        dici=model_cep.consulta_id(id)
        return dici
    except model_cep.NotFoundError:
        return {'erro':'cep nao cadastrado'},404

#Resolução da Q2
@app.route('/cep/excluir/<int:id>',methods=['DELETE'])
def rota_excluir(id):
    try:
        model_cep.excluir(id)
        return 'endereco excluido'
    except model_cep.NotFoundError:
        return {'erro':'cep nao cadastrado'},404

#Resolução da Q3
@app.route('/cep/cidade/<cidade>',methods=['GET'])
def rota_consulta_cidade(cidade):
    try:
        return model_cep.consulta_cidade(cidade)
    except model_cep.CidadeNaoEncontrada:
        return {'erro':'nao foi encontrado nenhum endereco para essa cidade'},404
    
@app.route('/cep/estado/<uf>',methods=['GET'])
def rota_consulta_estado(uf):
    try:
        return model_cep.consulta_estado(uf)
    except model_cep.EstadoNaoEncontrado:
        return {'erro':'nao foi encontrado nenhum endereco para esse estado'},404

#Resolução da Q5
#Exemplo dicionário válido={'CEP':'27251165','cidade':'Guaratingueta'}, apenas o CEP e a(s) chave(s) a alterar são necessários
@app.route('/cep/editar',methods=['PUT'])
def rota_editar():
    try:
        dici=request.json
        model_cep.editar(dici)
        return 'endereco alterado com sucesso'
    except model_cep.NotFoundError:
        return {'erro':'cep nao cadastrado'},404

app.run(host='0.0.0.0', port=5000, debug=True)
