from models import Base
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nome: str
    email: EmailStr
    senha_hash: str

