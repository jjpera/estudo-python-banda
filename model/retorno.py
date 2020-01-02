# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Retorno(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, codigo: int=None, descricao: str=None, registros: int=None, pagina: int=None, qtde_pagina: int=None):  # noqa: E501
        """Retorno - a model defined in Swagger

        :param codigo: The codigo of this Retorno.  # noqa: E501
        :type codigo: int
        :param descricao: The descricao of this Retorno.  # noqa: E501
        :type descricao: str
        :param registros: The registros of this Retorno.  # noqa: E501
        :type registros: int
        :param pagina: The pagina of this Retorno.  # noqa: E501
        :type pagina: int
        :param qtde_pagina: The qtde_pagina of this Retorno.  # noqa: E501
        :type qtde_pagina: int
        """
        self.swagger_types = {
            'codigo': int,
            'descricao': str,
            'registros': int,
            'pagina': int,
            'qtde_pagina': int
        }

        self.attribute_map = {
            'codigo': 'codigo',
            'descricao': 'descricao',
            'registros': 'registros',
            'pagina': 'pagina',
            'qtde_pagina': 'qtdePagina'
        }
        self._codigo = codigo
        self._descricao = descricao
        self._registros = registros
        self._pagina = pagina
        self._qtde_pagina = qtde_pagina

    @classmethod
    def from_dict(cls, dikt) -> 'Retorno':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Retorno of this Retorno.  # noqa: E501
        :rtype: Retorno
        """
        return util.deserialize_model(dikt, cls)

    @property
    def codigo(self) -> int:
        """Gets the codigo of this Retorno.


        :return: The codigo of this Retorno.
        :rtype: int
        """
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: int):
        """Sets the codigo of this Retorno.


        :param codigo: The codigo of this Retorno.
        :type codigo: int
        """

        self._codigo = codigo

    @property
    def descricao(self) -> str:
        """Gets the descricao of this Retorno.


        :return: The descricao of this Retorno.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str):
        """Sets the descricao of this Retorno.


        :param descricao: The descricao of this Retorno.
        :type descricao: str
        """

        self._descricao = descricao

    @property
    def registros(self) -> int:
        """Gets the registros of this Retorno.


        :return: The registros of this Retorno.
        :rtype: int
        """
        return self._registros

    @registros.setter
    def registros(self, registros: int):
        """Sets the registros of this Retorno.


        :param registros: The registros of this Retorno.
        :type registros: int
        """

        self._registros = registros

    @property
    def pagina(self) -> int:
        """Gets the pagina of this Retorno.


        :return: The pagina of this Retorno.
        :rtype: int
        """
        return self._pagina

    @pagina.setter
    def pagina(self, pagina: int):
        """Sets the pagina of this Retorno.


        :param pagina: The pagina of this Retorno.
        :type pagina: int
        """

        self._pagina = pagina

    @property
    def qtde_pagina(self) -> int:
        """Gets the qtde_pagina of this Retorno.


        :return: The qtde_pagina of this Retorno.
        :rtype: int
        """
        return self._qtde_pagina

    @qtde_pagina.setter
    def qtde_pagina(self, qtde_pagina: int):
        """Sets the qtde_pagina of this Retorno.


        :param qtde_pagina: The qtde_pagina of this Retorno.
        :type qtde_pagina: int
        """

        self._qtde_pagina = qtde_pagina
