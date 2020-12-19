from pydantic import BaseModel
class ConsultarReserva(BaseModel):
    email: str
    numero_documento: int


class AgregarReserva(BaseModel):
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