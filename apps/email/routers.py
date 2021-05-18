from fastapi import APIRouter

routerEmail = APIRouter(
    prefix='/email',
    tags=['Email']
    )

@routerEmail.get('/')
async def sendEmail():
    return {'hello':'email'}