from typing import Dict
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    nombre: str
    apellido: str
    email: str
    tipo_documento: str
    numero_documento: int
    numero_celular: int
    date_in: str
    date_out: str
    num_childs: int
    num_adults: int
    tipo_acomodacion: str


database_users = Dict[str,ReservaInDB]

database_users = {
    "pablotamayo44@gmail.com":ReservaInDB(**{"nombre":"Pablo", "apellido":"Tamayo",
    "email": "pablotamayo44@gmail.com","tipo_documento":"cedula", "numero_documento":1047477259,
    "numero_celular": 3188135533, "date_in":"23/12/2020", "date_out":"23/01/2021", "num_childs":0, 
    "num_adults":1,"tipo_acomodacion":"sencillo"})
}
# Consultar reservacion
def get_user(email: str):
    if email in database_users.keys():
        return database_users[email]
    else:
        return None

def add_user(reserva_in_db:ReservaInDB):
    database_users[reserva_in_db.email] = ReservaInDB(**{"nombre":reserva_in_db.nombre, "apellido":reserva_in_db.apellido,
    "email": reserva_in_db.email,"tipo_documento":reserva_in_db.tipo_documento, "numero_documento":reserva_in_db.numero_documento,
    "numero_celular": reserva_in_db.numero_celular,"date_in":reserva_in_db.date_in, "date_out":reserva_in_db.date_out,
    "num_childs":reserva_in_db.num_childs, "num_adults":reserva_in_db.num_adults,"tipo_acomodacion":reserva_in_db.tipo_acomodacion})
    return database_users

def actualizar_datos_reserva(actualizar_reserva_in_db:ReservaInDB):
    database_users[actualizar_reserva_in_db.email].date_in = actualizar_reserva_in_db.date_in
    database_users[actualizar_reserva_in_db.email].date_out = actualizar_reserva_in_db.date_out
    database_users[actualizar_reserva_in_db.email].num_childs = actualizar_reserva_in_db.num_childs
    database_users[actualizar_reserva_in_db.email].num_adults = actualizar_reserva_in_db.num_adults
    database_users[actualizar_reserva_in_db.email].tipo_acomodacion = actualizar_reserva_in_db.tipo_acomodacion

    return actualizar_reserva_in_db

def actualizar_datos_usuario_reserva(actualizar_usuario_in_db:ReservaInDB):
    database_users[actualizar_usuario_in_db.email].nombre = actualizar_usuario_in_db.nombre
    database_users[actualizar_usuario_in_db.email].apellido = actualizar_usuario_in_db.apellido
    database_users[actualizar_usuario_in_db.email].tipo_documento = actualizar_usuario_in_db.tipo_documento
    database_users[actualizar_usuario_in_db.email].numero_documento = actualizar_usuario_in_db.numero_documento
    database_users[actualizar_usuario_in_db.email].numero_celular = actualizar_usuario_in_db.numero_celular

    return actualizar_usuario_in_db
