import os
import requests
import json

from chilexpress.config import ENVIOS_TOKEN as TOKEN
from chilexpress.config import TCC
from chilexpress.config import TRANSPORT_ORDERS_URL as URL
from chilexpress.config import LABEL_TYPE
from chilexpress.core import _get, _post, _put


def get_certificate(number):
    ''' CONSULTA DE CERTIFICADOS '''
    url = f'{URL}transport-order-certificates/{number}'
    return _get(url, TOKEN)


def generate_certificate(card_number=TCC):
    ''' GENERACION DE CERTIFICADOS '''
    url = f'{URL}transport-order-certificates'
    params = {'customerCardNumber':card_number}
    return _post(url, TOKEN, params=params)


def generate_order(data):
    ''' GENERAR ORDEN DE TRANSPORTE '''
    url = f'{URL}transport-orders'
    return _post(url, TOKEN, data=data)


def get_order_label(data):
    ''' REIMPRESIÓN DE ETIQUETAS '''
    url = f'{URL}transport-orders-labels'
    return _post(url, TOKEN, data=data)


def track_order(data):
    ''' CONSULTA INDIVIDUAL DE ENVÍO '''
    url = f'{URL}tracking'
    return _post(url, TOKEN, data=data)


def close_certificate(number, certificate_type=2, drop_number=0):
    ''' CIERRE DE CERTIFICADO '''
    url = f'{URL}transport-order-certificates'
    data = {'certificateNumber': number, 'certificateType': certificate_type,
            'drop_number': drop_number}
    return _put(url, TOKEN, data=data)
