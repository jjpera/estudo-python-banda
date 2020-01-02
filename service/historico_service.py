import requests, json

url='http://localhost:8081/historico/historico'

def insert(tipoHistorico, banda):
    descricao = "velocidade: " + banda["velocidade"] + " tecnologia: " + banda["tecnologia"]
    headers = {'Content-type': 'application/json'}
    historico = {
        "tipo": tipoHistorico,
        "sistema": "banda",
        "descricao": descricao
    }

    response = requests.post(url, data=json.dumps(historico), headers=headers)

    print(response)

    return response