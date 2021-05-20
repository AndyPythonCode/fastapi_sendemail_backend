from decouple import config
from database.db import Conexion
from fastapi.middleware.cors import CORSMiddleware

# DESCRIPTION
API_METADATA = {
    'title': 'Curriculum Vitae',
    'description': 'Welcome Backend Curriculum Web',
    'version': '0.0.2'
}

# DATABASE
CONEXION = Conexion()

# SECURITY
MIDDLEWARE = {
    'middleware_class': CORSMiddleware,
    'allow_origins': config('HOST'),
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}

CREATE_TABLES = True

GMAIL_USER: str = config('USER')

GMAIL_PASSWORD: str = config('PASSWORD')
