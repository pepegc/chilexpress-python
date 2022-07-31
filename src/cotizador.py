from chilexpress.config import RATING_URL as URL
from chilexpress.config import COTIZADOR_TOKEN as TOKEN
from chilexpress.core import _post


def get_standard_quotation(data):
    ''' COTIZADOR ESTÁNDAR '''
    url = f'{URL}/rates/courier'
    return _post(url, TOKEN, data=data)


def get_business_quotation(data):
    ''' COTIZADOR EMPRESA '''
    url = f'{URL}/rates/business'
    return _post(url, TOKEN, data=data)

