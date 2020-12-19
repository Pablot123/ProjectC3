from typing import Dict
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    nombre: str
    apellido: str
    email: str

