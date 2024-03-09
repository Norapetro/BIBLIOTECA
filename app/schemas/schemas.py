from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, EmailStr, Field
from pydantic.generics import GenericModel
from datetime import date

# creamos un tipo de variable "cualquiera"
T = TypeVar("T")

# Creamos el esquema del libro
class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    author: str
    publication_date: str
    publisher: str
    num_pages: int
    description: Optional[str] = None
    price: float
    
    class Config:
        orm_mode = True           # le especificamos que será para uso de un ORM
        schema_extra = {         # Colocamos un ejemplo que se mostrará en el SWAGGER
            "example": {
                "id": 1,
                "title": "Título del libro",
                "author": "Autor del libro",
                "publication_date": "2022-03-01",
                "publisher": "Editorial",
                "num_pages": 200,
                "description": "Descripción del libro",
                "price": 19.99
            }
        }
class UserSchema(BaseModel):
    id: int
    cedula: str  # Número de cédula del usuario
    username: str  # Nombre de usuario único
    email: EmailStr  # Correo electrónico único
    phone: str  # Teléfono del usuario
    address: str  # Dirección del usuario
    
class BookTransactionSchema(BaseModel):
    user_id: int
    book_id: int
    date_transaction: date
    type_transaction: str    
    
    
# Creamos un schema de respuesta
class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]