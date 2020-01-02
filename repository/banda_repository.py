from repository import db

col = db["banda"]

def insert(banda):
    banda.id = col.insert_one(banda)
    return banda

def find(velocidade, tecnologia, pagina, qtdePagina):
    myquery = {}
    if velocidade != "" and tecnologia != "":
        myquery = {[{ "velocidade": velocidade }, { "tecnologia": tecnologia }]}
    elif velocidade != "":
        myquery = { "velocidade": velocidade }
    elif tecnologia != "":
        myquery = { "tecnologia": tecnologia }

    bandas = col.find(myquery).sort("tecnologia").skip(pagina*qtdePagina).limit((pagina+1)*qtdePagina)
    return bandas

def update(id, banda):
    myquery = { "_id": id }
    newvalues = { "$set": [{ "velocidade": banda.velocidade }, { "tecnologia": banda.tecnologia }] }

    col.update_one({myquery}, newvalues)
    return banda

def delete(id):

    banda = col.find_one({"_id" : id})

    col.delete_one({"_id" : id})

    return banda