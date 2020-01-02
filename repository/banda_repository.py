from repository import db

col = db["banda"]

def insert(banda):
    banda.id = col.insert_one(banda)
    return banda

def findById(id):
    return col.findOne({ "_id": id })

def find(velocidade, tecnologia, pagina, qtdePagina):
    bandas = col.find(generateQuery(velocidade, tecnologia))\
        .sort("tecnologia")\
        .skip(pagina*qtdePagina)\
        .limit((pagina+1)*qtdePagina)

    return bandas

def count(velocidade, tecnologia):
    return col.find(generateQuery(velocidade, tecnologia)).count(True)

def update(id, banda):
    newvalues = { "$set": [{ "velocidade": banda.velocidade }, { "tecnologia": banda.tecnologia }] }

    col.update_one({ "_id": id }, newvalues)
    return banda

def delete(id):
    col.delete_one({"_id" : id})
    return

def generateQuery(velocidade, tecnologia):
    query = {}
    if velocidade != "" and tecnologia != "":
        query = {[{ "velocidade": velocidade }, { "tecnologia": tecnologia }]}
    elif velocidade != "":
        query = { "velocidade": velocidade }
    elif tecnologia != "":
        query = { "tecnologia": tecnologia }
    return query