from pydantic import BaseModel
class UserIn(BaseModel):
    email: str
    password: str

class UserAdd(BaseModel):
    nombre: str
    apellido: str
    email: str
    tipo_documento: str
    numero_documento: int
    numero_celular: int
    password: str