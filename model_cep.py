'''
Lista de CEPs e endereços. 
Cada entidade tem CEP, endereço, estado, cidade e outros atributos que achar conveniente. Pode usar o CEP como ID
'''

lista_ceps=[
    {
        'CEP':'02474130',
        'endereco':'Rua Edmundo Kirmayr',
        'estado':'SP',
        'cidade':'São Paulo'
    },
    {
        'CEP':'02536000',
        'endereco':'Rua Jorge Valim',
        'estado':'SP',
        'cidade':'São Paulo'
    }
]

class NotFoundError(Exception):
    pass

class CidadeNaoEncontrada(Exception):
    pass

class EstadoNaoEncontrado(Exception):
    pass

class JaCadastradoError(Exception):
    pass

def todos():
    return lista_ceps

def consulta_id(id):
    for item in lista_ceps:
        if int(item['CEP'])==int(id):
            return item
    raise NotFoundError

def adiciona(dici):
    try:
        consulta_id(dici['CEP'])
    except NotFoundError:    
        lista_ceps.append(dici)
        return
    raise JaCadastradoError

def excluir(id):
    consulta_id(id)

    for item in lista_ceps:
        if int(item['CEP'])==int(id):
            index=lista_ceps.index(item)
            del lista_ceps[index]
            return

def consulta_cidade(cidade):
    lista_itens=[]
    for item in lista_ceps:
        if item['cidade']==cidade:
            lista_itens.append(item)
    if lista_itens!=[]:
        return lista_itens
    raise CidadeNaoEncontrada

def consulta_estado(uf):
    lista_itens=[]
    for item in lista_ceps:
        if item['estado']==uf:
            lista_itens.append(item)
    if lista_itens!=[]:
        return lista_itens
    raise EstadoNaoEncontrado

def editar(dici):
    consulta_id(dici['CEP'])
    for item in lista_ceps:
        if item['CEP']==dici['CEP']:
            for chave in dici:
                if item[chave]!=dici.get(chave):
                    item[chave]=dici[chave]
            return
