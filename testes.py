import requests

url_server = 'http://127.0.0.1:5000/'

def test_todos():
    url=f'{url_server}/cep/todos'
    r=requests.get(url)
    print(r.status_code)
    print(r.json())

def test_add(dici):
    url=f'{url_server}/cep/adiciona'
    r=requests.post(url,json=dici)
    print(r.status_code)
    print(r.text)

def test_consulta_id(id):
    url=f'{url_server}/cep/{id}'
    r=requests.get(url)
    print(r.status_code)
    print(r.json())

def test_excluir(id):
    url=f'{url_server}/cep/excluir/{id}'
    r=requests.delete(url)
    print(r.status_code)
    print(r.text)

def test_consulta_cidade(cidade):
    url=f'{url_server}/cep/cidade/{cidade}'
    r=requests.get(url)
    print(r.status_code)
    print(r.json())

def test_alterar(dici):
    url=f'{url_server}/cep/editar'
    r=requests.put(url,json=dici)
    print(r.status_code)
    print(r.text)

rc={'CEP':'27251165','endereco':'Rua C','estado':'RJ','cidade':'Volta Redonda'}

test_todos()
test_add(rc)
test_todos()
print('================')

test_consulta_id(27251165)
print('================')

test_excluir(27251165)
test_todos()
print('================')

test_consulta_cidade('São Paulo')
test_consulta_cidade('Volta Redonda')
print('================')

ek2={
    'CEP':'02474130',
    'cidade':'Guarulhos'
    }
test_alterar(ek2)
test_todos()