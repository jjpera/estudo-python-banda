#import markdown
#import os
#import shelve

#from flask import Flask, g
#from flask_restful import Resource, Api, reqparse

from flask_restful import Resource
from flask import request
from service import banda_service

class Banda(Resource):
    def get(self):
        velocidade = request.args.get("velocidade")
        tecnologia = request.args.get("tecnologia")
        pagina = request.args.get("pagina")
        qtdepagina = request.args.get("qtdePagina")

        return banda_service.find(velocidade, tecnologia, pagina, qtdepagina) , 200

    def post(self):
        banda = {
            "velocidade": request.form.get("velocidade"),
            "tecnologia": request.form.get("tecnologia")
        }

        return banda_service.insert(banda) , 200

class BandaId(Resource):
    def update(self, identifier):
        banda = {
            "_id": request.form.get("id"),
            "velocidade": request.form.get("velocidade"),
            "tecnologia": request.form.get("tecnologia")
        }

        return banda_service.update(identifier, banda), 200

    def delete(self, identifier):
        return banda_service.delete(identifier), 200
