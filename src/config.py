import os

TCC = os.getenv('CHILEXPRESS_TCC')
RUT = os.getenv('CHILEXPRESS_RUT')

COBERTURA_TOKEN = os.getenv('CHILEXPRESS_COBERTURA_TOKEN')
COTIZADOR_TOKEN = os.getenv('CHILEXPRESS_COTIZADOR_TOKEN')
ENVIOS_TOKEN = os.getenv('CHILEXPRESS_ENVIOS_TOKEN')

API_VERSION = os.getenv('CHILEXPRESS_API_VERSION')
ROOT_URL = os.getenv('CHILEXPRESS_ROOT_URL')
GEOREFERENCE_URL = f'{ROOT_URL}georeference/api/v{API_VERSION}/'
RATING_URL = f'{ROOT_URL}rating/api/v{API_VERSION}/'
TRANSPORT_ORDERS_URL = f'{ROOT_URL}transport-orders/api/v{API_VERSION}/'

SERVICES = {
    'Prioritario': {
        'short': 'PREX',
        'code': 2,
        'description':(
            'Entrega el día hábil siguiente, hasta las 19:00 horas'
        )
    },
    'Express': {
        'short': 'CHEX', #CHEX, CLEX ??
        'code': 3,
        'description':(
            'Entrega en 1 a 2 días hábiles, hasta las 19:00 horas'
        )
    },
    'Extendido': {
        'short': 'XTEN',
        'code': 4,
        'description':(
            'Entrega en 2 a 4 días hábiles, hasta las 19:00 horas'
        )
    },
    'Extremos': {
        'short': 'XTRE',
        'code': 5,
        'description':(
            'Entrega en 3 a 5 días hábiles, hasta las 19:00 horas'
        )
    }
}

LABEL_TYPE= {
    'none': {
        'code': 0,
        'description': 'Solo Datos'
    },
    'epl': {
        'code': 1,
        'description': 'EPL Impresora Zebra + datos'
    },
    'bin': {
        'code': 2,
        'description': 'Imagen en binario + datos'
    }
}

PRODUCT_TYPE= {
    'moda': {
        'code': 1,
        'description': 'Moda',
        'response': 'x'
    },
    'tecnologia': {
        'code': 2,
        'description': 'Tecnología',
        'response': 'x'
    },
    'repuestos': {
        'code': 3,
        'description': 'Repuestos',
        'response': 'x'
    },
    'medicos': {
        'code': 4,
        'description': 'Productos médicos',
        'response': 'x'
    },
    'otros': {
        'code': 5,
        'description': 'Otros',
        'response': 'R'
    }
}
