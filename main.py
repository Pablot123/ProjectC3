from db.user_db import ReservaInDB
from db.user_db import add_user, get_user, actualizar_datos_reserva,actualizar_datos_usuario_reserva
from models.user_models import ConsultarReserva, AgregarReserva, ActualizarReserva, ActializarDatosUsuario

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.post("/consultar/")
async def auth_user(user_in:ConsultarReserva):
    user_in_db = get_user(user_in.email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
        detail="El correo no existe")
    if user_in_db.numero_documento != user_in.numero_documento:
        raise HTTPException(status_code=404,
        detail="El numero de documento esta errado")

    return user_in_db.nombre, user_in_db.apellido, user_in_db.email, user_in_db.date_in, user_in_db.date_out, user_in_db.num_childs, user_in_db.num_adults, user_in_db.tipo_acomodacion


@api.post("/reservar/")
async def agregar_reserva(user_in:AgregarReserva):
    user_in_db = get_user(user_in.email)
    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El usuario con ese correo ya existe")
        #return {"Agregado_correctamente":False}
    else:
        add_user(user_in)
        return {"Agregado_correctamente":True}
    
@api.put("/actualizar/reserva/")
async def actualizar_reserva(datos_reserva_in:ActualizarReserva):
    reserva_in_db = get_user(datos_reserva_in.email)
    if reserva_in_db == None:
        raise HTTPException(status_code=404,
        detail="El correo no existe")
    elif reserva_in_db.numero_documento != datos_reserva_in.numero_documento:
        raise HTTPException(status_code=404,
        detail="El numero de documento esta errado")
    else:
        actualizar_datos_reserva(datos_reserva_in)
        return {"exito_actualizacion_reserva":True}

@api.put("/actualizar/datos_usuario/")
async def actualizar_datos_usuario_(datos_usuario_in:ActializarDatosUsuario):
    datos_usuario_in_db = get_user(datos_usuario_in.email)
    if datos_usuario_in_db == None:
        raise HTTPException(status_code=404,
        detail="El correo no existe")
    elif datos_usuario_in_db.numero_documento != datos_usuario_in.numero_documento:
        raise HTTPException(status_code=404,
        detail="El numero de documento esta errado")
    else:
        actualizar_datos_usuario_reserva(datos_usuario_in)
        return {"exito_actualizacion_usuario":True}




        


