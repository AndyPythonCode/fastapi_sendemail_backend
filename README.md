## PACKAGE
    uvicorn
    fastapi
    python-decouple
    databases
    asyncpg
    psycopg2
    pydantic[email]

## MODULES
    main.py -> it is root file, the executable
    db.py -> where it is our database configuration 
    manage.py -> every configuration like middleware, description, routers, etc...
    apps -> it is a folder to wrap every single api
        models.py -> configuration for the tables in database
        schemas.py -> validate data input
        routers.py -> router for a especific path

# Gunicorn con trabajadores de Uvicorn
    Requests per second:    8665.48 [#/sec] (mean)
    Concurrency Level:      500
    Time taken for tests:   0.577 seconds
    Complete requests:      5000
    Time per request:       57.700 [ms] (mean)

# Uvicorn puro
    Requests per second:    3200.62 [#/sec] (mean)
    Concurrency Level:      500
    Time taken for tests:   1.562 seconds
    Complete requests:      5000
    Time per request:       156.220 [ms] (mean)
Como puede ver, hay una gran diferencia en RPS (Solicitud por segundo) y tiempo de respuesta para cada solicitud.

## Procfiles
* __Gunicorn con trabajadores de Uvicorn__

web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

* __Uvicorn puro__

web: uvicorn main:app --workers 4

La (s) respuesta (s) son correctas, pero usar FastAPI en producción ejecutándose como WSGI con trabajadores ASGI es una mejor opción. Por eso, ejecuté un punto de referencia para esta pregunta , así que aquí están los resultados.