from repository import db
from util import ModelBanda
from bson import ObjectId

col = db["banda"]

def insert(banda):
    print("insert:" + banda["velocidade"] + " - " + banda["tecnologia"])

    col.insert_one(banda)

    return banda

def findById(id):
    print("findById:" + id)
    cursor = col.find({ "_id": ObjectId(id) })
    if cursor.count() != 1:
        raise Exception("Id não encontrado")

    return cursor[0]

def find(velocidade, tecnologia, pagina, qtdePagina):
    print("velocidade: " + velocidade + " tecnologia: " + tecnologia + " pagina: " + str(pagina) + " qtdePagina: " + str(qtdePagina))

    bandas = col.find(ModelBanda.generateQuery(velocidade, tecnologia))\
        .sort("tecnologia")\
        .skip(pagina*qtdePagina)\
        .limit((pagina+1)*qtdePagina)

    return list(bandas)

def count(velocidade, tecnologia):
    return col.find(ModelBanda.generateQuery(velocidade, tecnologia)).count(True)

def update(id, banda):
    newvalues = { "$set": { "velocidade": banda["velocidade"], "tecnologia": banda["tecnologia"] } }

    col.update_one({ "_id": ObjectId(id) }, newvalues)
    banda["_id"] = ObjectId(id)

    return banda

def delete(id):
    col.delete_one({"_id" : ObjectId(id)})
    return
