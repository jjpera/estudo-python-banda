import connexion
import six

from swagger_server.models.banda import Banda  # noqa: E501
from swagger_server.models.retorno_banda import RetornoBanda  # noqa: E501
from swagger_server.models.tecnologia import Tecnologia  # noqa: E501
from swagger_server import util


def alterar_banda(body, codigo):  # noqa: E501
    """Alterar Banda Larga

    Alterar Banda Larga. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param codigo: 
    :type codigo: int

    :rtype: RetornoBanda
    """
    if connexion.request.is_json:
        body = Banda.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def buscar_banda(pagina, qtde_pagina, velocidade=None, tecnologia=None):  # noqa: E501
    """Buscar Banda Larga

    Buscar Banda Larga. # noqa: E501

    :param pagina: 
    :type pagina: int
    :param qtde_pagina: 
    :type qtde_pagina: int
    :param velocidade: 
    :type velocidade: str
    :param tecnologia: 
    :type tecnologia: dict | bytes

    :rtype: RetornoBanda
    """
    if connexion.request.is_json:
        tecnologia = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cadastrar_banda(body):  # noqa: E501
    """Cadastrar Banda Larga

    Cadastrar Banda Larga. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: RetornoBanda
    """
    if connexion.request.is_json:
        body = Banda.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def excluir_banda(codigo):  # noqa: E501
    """Excluir Banda Larga

    Excluir Banda Larga. # noqa: E501

    :param codigo: 
    :type codigo: int

    :rtype: RetornoBanda
    """
    return 'do some magic!'
