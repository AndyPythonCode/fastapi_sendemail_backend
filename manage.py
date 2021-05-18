from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from apps.email.routers import routerEmail

# DESCRIPTION
API_METADATA = {
    'title': 'Curriculum Vitae',
    'description': 'Welcome Backend Curriculum Web',
    'version': '0.0.2'
}

# ROUTERS
URL_PATTERNS = (routerEmail,)

# SECURITY
MIDDLEWARE = {
    'middleware_class': CORSMiddleware,
    'allow_origins': config('HOST'),
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}
