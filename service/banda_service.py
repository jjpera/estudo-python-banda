from repository import banda_repository
from util import ModelBanda
from service import historico_service

def insert(banda):
    retornoBanda = {}
    try:
        banda = banda_repository.insert(banda)

        historico_service.insert("post", banda)

        retornoBanda = ModelBanda.retornoBandaDefault()
        retornoBanda["lista_bandas"] = [banda]
    except Exception as e:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro: " + str(e)
        }

    return retornoBanda

def find(velocidade, tecnologia, pagina, qtdePagina):
    retornoBanda = {}
    try:
        bandas = banda_repository.find(velocidade, tecnologia, pagina, qtdePagina)

        historico_service.insert("get", {"velocidade": velocidade, "tecnologia": tecnologia})

        retornoBanda = ModelBanda.retornoBandaDefaultParam(pagina, qtdePagina)
        retornoBanda["lista_bandas"] = bandas
        retornoBanda["registros"] = banda_repository.count(velocidade, tecnologia)
    except Exception as e:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro: " + str(e)
        }

    return retornoBanda

def update(id, banda):
    retornoBanda = {}
    try:
        banda_repository.findById(id)

        banda = banda_repository.update(id, banda)

        historico_service.insert("put", banda)

        retornoBanda = ModelBanda.retornoBandaDefault()
        retornoBanda["lista_bandas"] = [banda]
    except Exception as e:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro: " + str(e)
        }

    return retornoBanda

def delete(id):
    retornoBanda = {}
    try:
        banda = banda_repository.findById(id)

        banda_repository.delete(id)

        historico_service.insert("delete", banda)

        retornoBanda = ModelBanda.retornoBandaDefault()
        retornoBanda["lista_bandas"] = [banda]
    except Exception as e:
        retornoBanda = {
            "codigo": 500,
            "descricao": "Erro: " + str(e)
        }

    return retornoBanda
