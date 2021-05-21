from .models import *
from fastapi import APIRouter
from manage import GMAIL_USER, GMAIL_PASSWORD
from email.message import EmailMessage
from .schemas import Email
import smtplib

routerEmail = APIRouter(
    prefix='/email',
    tags=['Email']
)

@routerEmail.post('/')
async def sendEmail(request: Email):
    # Drawing up
    msg_user = EmailMessage()
    msg_me = EmailMessage()

    # Send custom email to user
    msg_user.set_content(f"""
From: {GMAIL_USER}
To: {request.email}

Gracias por contactar conmigo, su mensaje me ha llegado!!!

Contactaré con usted lo mas pronto posible desde mi correo personal andyarciniegas24@gmail.com
Aca dejo mi WhatsApp: +1 (829-958-0083)

Suerte!!!!
    """)

    status_user = sending('Enviado!', GMAIL_USER, request.email, msg_user)

    # Send custom email to my account
    msg_me.set_content(f"""
Hi i'm: {GMAIL_USER}
    
This user {request.email} want to talk with you.

{request.message}

{GMAIL_USER}, I will be around, bye bye...
    """)

    status_me = sending(request.title, GMAIL_USER, 'andyarciniegas24@gmail.com', msg_me)

    # added to database
    query = email.insert().values(**request.dict())
    last_record_id = await CONEXION.getDataBase().execute(query)
    return {'id': last_record_id, **request.dict(), 'email': {'user': status_user, 'me': status_me}}

def sending(SUBJECT, FROM, TO, MSG):
    try:
        MSG['Subject'] = SUBJECT
        MSG['From'] = FROM
        MSG['To'] = TO
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(MSG)
        server.quit()
    except:
        return False
    return True