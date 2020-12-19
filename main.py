from db.user_db import ReservaInDB
from db.user_db import add_user, get_user
from models.user_models import ConsultarReserva, AgregarReserva

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

    return {"Consulta_exitosa":True}


@api.post("/reservar/")
async def save_NewUser(user_in:AgregarReserva):
    user_in_db = get_user(user_in.email)
    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El usuario con ese correo ya existe")
        #return {"Agregado_correctamente":False}
    else:
        add_user(user_in)
        return {"Agregado_correctamente":True}
    
    
        


