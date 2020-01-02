import json

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class ModelBanda():
    def retornoBandaDefault():
        return ModelBanda.retornoBandaDefaultParam(0, 1)
    def retornoBandaDefaultParam(pagina, qtde_pagina):
        return {
            'codigo': 0,
            'descricao': "success",
            'registros': 0,
            'pagina': pagina,
            'qtde_pagina': qtde_pagina
        }
    def generateQuery(velocidade, tecnologia):
        query = {}

        if velocidade != "":
            query["velocidade"] = {'$regex': velocidade}

        if tecnologia != "":
            query["tecnologia"] = tecnologia

        return query