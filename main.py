from fastapi import FastAPI
from path import URL_PATTERNS
from manage import (CONEXION,
                    API_METADATA,
                    MIDDLEWARE,
                    CREATE_TABLES)

# Application
app = FastAPI(**API_METADATA)

# Security
app.add_middleware(**MIDDLEWARE)

# Routers
for path in URL_PATTERNS:
    app.include_router(path)

# Create Tables
if CREATE_TABLES:
    CONEXION.createTables()

# When get in
@app.on_event("startup")
async def startup():
    await CONEXION.getDataBase().connect()


# When get out
@app.on_event("shutdown")
async def shutdown():
    await CONEXION.getDataBase().disconnect()


# Main routers
@app.get('/', tags=['Home'])
async def root():
    return 'API'
