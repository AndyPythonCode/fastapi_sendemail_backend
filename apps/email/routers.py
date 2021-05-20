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
    msg = EmailMessage()

    msg.set_content(f"""
        From: {GMAIL_USER}
        To: {request.email}

        {request.message}
    """)

    msg['Subject'] = request.title
    msg['From'] = GMAIL_USER
    msg['To'] = request.email

    # Send email
    status = sending(msg)

    # added to database
    query = email.insert().values(**request.dict())
    last_record_id = await CONEXION.getDataBase().execute(query)
    return {'id': last_record_id, **request.dict(), 'sent_email': status}


def sending(msg):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        return False
    return True