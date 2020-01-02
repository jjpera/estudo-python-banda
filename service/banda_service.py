from repository import banda_repository

def insert(banda):
    retornoBanda = {}
    try:
        banda = banda_repository.insert(banda)

        # se funcionar, chamar serviço rest de historico
        # serviceHistorico.insert(historico)

        retornoBanda = retornoBandaDefault()
        retornoBanda.lista_bandas = [banda]
    except:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro ao salvar registro"
        }
    
    return retornoBanda

def find(velocidade, tecnologia, pagina, qtdePagina):
    retornoBanda = {}
    try:
        bandas = banda_repository.find(velocidade, tecnologia, pagina, qtdePagina)

        # se funcionar, chamar serviço rest de historico
        # serviceHistorico.insert(historico)

        retornoBanda = retornoBandaDefault()
        retornoBanda.lista_bandas = bandas
    except:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro ao buscar registros"
        }
    
    return retornoBanda

def update(id, banda):
    retornoBanda = {}
    try:
        banda = banda_repository.update(id, banda)

        # se funcionar, chamar serviço rest de historico
        # serviceHistorico.insert(historico)

        retornoBanda = retornoBandaDefault()
        retornoBanda.lista_bandas = [banda]
    except:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro ao atualizar registro"
        }
    
    return retornoBanda

def delete(id):
    retornoBanda = {}
    try:
        banda = banda_repository.findById(id)
        
        banda_repository.delete(id)

        # se funcionar, chamar serviço rest de historico
        # serviceHistorico.insert(historico)

        retornoBanda = retornoBandaDefault()
        retornoBanda.lista_bandas = [banda]
    except:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro ao remover registro"
        }
    
    return retornoBanda

def retornoBandaDefault():
    return retornoBandaDefaultParam(0, 1)

def retornoBandaDefaultParam(pagina, qtde_pagina):
    return {
        'codigo': 0,
        'descricao': "success",
        'registros': 0,
        'pagina': pagina,
        'qtde_pagina': qtde_pagina
    }