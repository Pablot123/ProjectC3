from db.user_db import UserInDB
from db.user_db import add_user, get_user
from models.user_models import UserIn, UserAdd

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
        detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.post("/user/register/")
async def save_NewUser(user_in: UserAdd):
    user_in_db = get_user(user_in.email)
    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El usuario con ese correo ya existe")
        return {"Agregado_correctamente":False}
    else:
        add_user(user_in.nombre,user_in.apellido,user_in.email,user_in.tipo_documento,
        user_in.numero_documento,user_in.numero_celular,user_in.password)
        return {"Agregado_correctamente":True}
    
    
        


