import json
import requests

from chilexpress.config import ENVIOS_TOKEN as TOKEN

def _get(url, token, params=None):
    r = requests.get(url, headers=__headers(token), params=params)
    return r.json()


def _post(url, token, data=None, params=None):
    r = requests.post(
        url, headers=__headers(token), data=json.dumps(data), params=params)
    return r.json()


def _put(url, token, data=None, params=None):
    r = requests.put(
        url, headers=__headers(token), data=json.dumps(data), params=params)
    return r.json()


def _delete(url, token, params=None):
    r = requests.delete(
        url, headers=__headers(token), params=params)
    return r.json()


def __headers(token):
    return {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': token,
    }
