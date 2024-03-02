from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.db.config import SessionLocal,get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import BookSchema, Response, UserSchema
from app.db import crud
from app.db.config import get_db
from app.routes.routes import UserSchema

from app.db import crud

# Creamos un router, que es un conjunto de rutas agrupadas
router = APIRouter()

# Cabe mencionar que vamos a usar constantemente dos parametros 
# "request" el cual es la entrada y será acorde con el esquema "mostrar en SWAGGER"
# y "db" que es de tipo Sesion y de la cual depende de la conexión de nuestr db

# haremos uso de las funciones que creamos en el archivo de crud.py

# Creamos la ruta con la que crearemos 
@router.post("/create")
async def create_book_service(request: BookSchema, db: Session = Depends(get_db)):
    crud.create_book(db, book=request)
    print(request)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully",result=request).dict(exclude_none=True)
    # retornamos la respuesta con el schema de response


@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)


@router.patch("/update")
async def update_book(request: BookSchema, db: Session = Depends(get_db)):
    try:
        _book = crud.update_book(db, book_id=request.id,
                                title=request.title, description=request.description)
        return Response(status="Ok", code="200", message="Success update data", result=_book)
    except Exception as e:
        return Response(
            status="bad",
            code="304",
            message="the updated gone wrong"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db


@router.delete("/delete")
async def delete_book(request: BookSchema,  db: Session = Depends(get_db)):
    try:
        crud.remove_book(db, book_id=request.id)
        return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
    except Exception as e:
        return Response(
            status="bad",
            code="",
            message="the deleted gone wrong"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db
    
    
# Rutas CRUD para la entidad User
# @router.post("/users/create")
# async def create_user(user: UserSchema, db: Session = Depends(get_db)):
#     created_user = crud.create_user(db, user=user)
#     return Response(status="Ok", code="200", message="User created successfully", result=created_user).dict(exclude_none=True)

# @router.get("/users/")
# async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip, limit)
#     return Response(status="Ok", code="200", message="Success fetch all users", result=users)

# @router.patch("/users/update")
# async def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
#     updated_user = crud.update_user(db, user_id=user_id, user=user)
#     return Response(status="Ok", code="200", message="User updated successfully", result=updated_user)

# @router.delete("/users/delete")
# async def delete_user(user_id: int, db: Session = Depends(get_db)):
#     deleted_user = crud.delete_user(db, user_id=user_id)
#     return Response(status="Ok", code="200", message="User deleted successfully", result=deleted_user)
    