from fastapi import APIRouter, Depends, Response
from app.db import crud
from app.schemas.schemas import UserSchema
from app.db.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# Rutas CRUD para la entidad User
@router.post("/users/create")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    created_user = crud.create_user(db, user=user)
    return Response(status="Ok", code="200", message="Usuario creado con éxito", result=created_user).dict(exclude_none=True)

@router.get("/users/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return Response(status="Ok", code="200", message="Trae todos los usuarios con exito", result=users)

@router.patch("/users/update")
async def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id=user_id, user=user)
    return Response(status="Ok", code="200", message="Usuario actualizado con éxito", result=updated_user)

@router.delete("/users/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id=user_id)
    return Response(status="Ok", code="200", message="Usuario eliminado exitosamente", result=deleted_user)
    