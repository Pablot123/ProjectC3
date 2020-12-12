from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    nombre: str
    apellido: str
    email: str
    tipo_documento: str
    numero_documento: int
    numero_celular: int
    password: str

database_users = Dict[str,UserInDB]

database_users = {
    "pablotamayo44@gmail.com":UserInDB(**{"nombre":"Pablo", "apellido":"Tamayo",
    "email": "pablotamayo44@gmail.com","tipo_documento":"cedula", "numero_documento":1047477259,
    "numero_celular": 3188135533,"password":"hola"})
}
# iniciar sesion
def get_user(email: str):
    if email in database_users.keys():
        return database_users[email]
    else:
        return None

def add_user(nombre: str, apellido:str, email:str, tipo_documento:str, numero_documento: int, numero_celular: int, password:str):
    database_users[email] = UserInDB(**{"nombre":nombre, "apellido":apellido,
    "email": email,"tipo_documento":tipo_documento, "numero_documento":numero_documento,
    "numero_celular": numero_celular,"password":password})
    return database_users
