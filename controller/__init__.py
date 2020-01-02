#import markdown
#import os
#import shelve

#from flask import Flask, g
#from flask_restful import Resource, Api, reqparse

from flask_restful import Resource
from flask import request

class Banda(Resource):
    def get(self):
        velocidade = request.args.get("velocidade")
        tecnologia = request.args.get("tecnologia")
        pagina = request.args.get("pagina")
        qtdepagina = request.args.get("qtdePagina")

        return 'velocidade: ' + velocidade + ' tecnologia: ' + tecnologia + ' pagina: ' + pagina + ' qtdepagina: ' + qtdepagina , 200

    def post(self):
        return 'OK' , 200

class BandaId(Resource):
    def update(self, identifier):
        return 'OK', 200

    def delete(self, identifier):
        return 'OK', 200
