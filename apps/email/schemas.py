from pydantic import BaseModel
from pydantic.networks import EmailStr

class Email(BaseModel):
    title: str
    email:EmailStr
    message: str