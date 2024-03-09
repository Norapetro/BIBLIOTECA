from datetime import datetime
from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.db.config import SessionLocal,get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import BookSchema, BookTransactionSchema, Response, UserSchema
from app.db import crud
from app.db.config import get_db
from app.routes.routes import UserSchema
from ..models.models import Biblioteca

from app.db import crud
biblioteca = Biblioteca()

# Creamos un router, que es un conjunto de rutas agrupadas
router = APIRouter()

# Cabe mencionar que vamos a usar constantemente dos parametros 
# "request" el cual es la entrada y será acorde con el esquema "mostrar en SWAGGER"
# y "db" que es de tipo Sesion y de la cual depende de la conexión de nuestr db

# haremos uso de las funciones que creamos en el archivo de crud.py

# Creamos la ruta con la que crearemos 
@router.post("/create")
async def create_book_service(request: BookSchema, db: Session = Depends(get_db)):
    request.publication_date = datetime.strptime(request.publication_date, '%Y-%m-%d').date()
    crud.create_book(db, book=request)
    biblioteca.agregar_libro(request)
    print(request)
    return Response(status="Ok",
                    code="200",
                    message="Libro creado exitosamente",result=request).dict(exclude_none=True)
    # retornamos la respuesta con el schema de response


@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Se obtuvieron todos los datos con éxito", result=_books)

@router.get("/{book_id}")
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.patch("/update")
async def update_book(request: BookSchema, db: Session = Depends(get_db)):
    try:
        _book = crud.update_book(db, book_id=request.id,
                                title=request.title, description=request.description)
        return Response(status="Ok", code="200", message="Actualización de Datos exitosa", result=_book)
    except Exception as e:
        return Response(
            status="bad",
            code="304",
            message="la actualización salió mal"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db


@router.delete("/delete")
async def delete_book(request: BookSchema,  db: Session = Depends(get_db)):
    try:
        crud.remove_book(db, book_id=request.id)
        return Response(status="Ok", code="200", message="Eliminación exitosa de datos.").dict(exclude_none=True)
    except Exception as e:
        return Response(
            status="bad",
            code="",
            message="Algo en la eliminacion salio mal"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db