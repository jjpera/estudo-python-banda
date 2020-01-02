#import markdown
#import os
#import shelve

#from flask import Flask, g
#from flask_restful import Resource, Api, reqparse

from flask_restful import Resource
from flask import request, jsonify
from service import banda_service
from util import JSONEncoder

class Banda(Resource):
    def get(self):
        velocidade = request.args.get("velocidade")
        tecnologia = request.args.get("tecnologia")
        pagina = request.args.get("pagina")
        qtdepagina = request.args.get("qtdePagina")

        if not velocidade:
            velocidade = ""

        if not tecnologia:
            tecnologia = ""

        return JSONEncoder().encode(banda_service.find(velocidade, tecnologia, int(pagina), int(qtdepagina))), 200

    def post(self):
        return JSONEncoder().encode(banda_service.insert(request.json)), 200

class BandaId(Resource):
    def put(self, id):
        return JSONEncoder().encode(banda_service.update(id, request.json)), 200

    def delete(self, id):
        return JSONEncoder().encode(banda_service.delete(id)), 200

