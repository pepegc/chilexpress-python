import json
import os
import requests

from chilexpress.config import API_VERSION as API_VERSION
from chilexpress.config import COBERTURA_TOKEN as TOKEN
from chilexpress.config import GEOREFERENCE_URL as URL
from chilexpress.core import _get, _post


def get_regions():
    ''' CONSULTAR REGIONES '''
    url = f'{URL}regions'
    return _get(url, TOKEN)['regions'] #TODO


def get_counties(region_code, type):
    ''' CONSULTAR COBERTURAS '''
    url = f'{URL}coverage-areas'
    params = {'RegionCode': region_code, 'type': type}
    return _get(url, TOKEN, params=params)['coverageAreas'] #TODO


def get_pickups(region_code, county_name, type=0):
    ''' OFICINAS DE ENTREGA '''
    #type:  0: Sucursales propias / 4: Tiendas Pick Up
    url = f'{URL}offices'
    params = {'RegionCode':region_code, 'CountyName':county_name, 'Type':type}
    return _get(url, TOKEN, params=params)


def get_numeraciones(street_id, street_number):
    ''' CONSULTAR NUMERACIONES '''
    url = f'{URL}streets/{street_id}/numbers'
    params = {'streetNumber': street_number}
    return _get(url, TOKEN, params=params)


def get_streets(county_name, street_name, limit=5):
    ''' CONSULTAR CALLES '''
    url = f'{URL}streets/search'
    params = {'limit': limit}
    data = {'countyName':county_name, 'streetName':street_name}
    return _post(url, TOKEN, data=data, params=params)


def get_coordinates(county_name, street_name, number):
    ''' GEOREFERENCIAR UNA DIRECCIÓN '''
    url = f'{URL}addresses/georeference'
    data = {'countyName':county_name, 'streetName':street_name, 'number':number}
    return _post(url, TOKEN, data=data)
