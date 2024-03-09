from fastapi import APIRouter, Depends, HTTPException, Path
from app.db import crud
from app.schemas.schemas import UserSchema, Response
from app.db.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# Rutas CRUD para la entidad User
@router.post("/create")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    created_user = crud.create_user(db, user=user)
    return Response(status="Ok", code="200", message="User created successfully", result=created_user).dict(exclude_none=True)

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=users)

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/update")
async def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id=user_id, user=user)
    return Response(status="Ok", code="200", message="Success update data", result=updated_user)

@router.delete("/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id=user_id)
    return Response(status="Ok", code="200", message="Success delete data", result=deleted_user)
    