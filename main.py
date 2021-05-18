from sys import prefix
from fastapi import FastAPI
from manage import (API_METADATA,
                    URL_PATTERNS,
                    MIDDLEWARE)

app = FastAPI(**API_METADATA)

app.add_middleware(**MIDDLEWARE)

for path in URL_PATTERNS:
    app.include_router(path)


@app.get('/', tags=['Home'])
async def root():
    return {'Welcome': 'User'}
