# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.banda import Banda  # noqa: E501
from swagger_server.models.retorno_banda import RetornoBanda  # noqa: E501
from swagger_server.models.tecnologia import Tecnologia  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBandaLargaController(BaseTestCase):
    """BandaLargaController integration test stubs"""

    def test_alterar_banda(self):
        """Test case for alterar_banda

        Alterar Banda Larga
        """
        body = Banda()
        response = self.client.open(
            '/bandas/banda/{codigo}'.format(codigo=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_buscar_banda(self):
        """Test case for buscar_banda

        Buscar Banda Larga
        """
        query_string = [('velocidade', 'velocidade_example'),
                        ('tecnologia', Tecnologia()),
                        ('pagina', 56),
                        ('qtde_pagina', 56)]
        response = self.client.open(
            '/bandas/banda',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cadastrar_banda(self):
        """Test case for cadastrar_banda

        Cadastrar Banda Larga
        """
        body = Banda()
        response = self.client.open(
            '/bandas/banda',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_excluir_banda(self):
        """Test case for excluir_banda

        Excluir Banda Larga
        """
        response = self.client.open(
            '/bandas/banda/{codigo}'.format(codigo=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
