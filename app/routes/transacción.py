from fastapi import APIRouter, Depends
from app.db import crud
from app.schemas.schemas import BookTransactionSchema, Response
from app.db.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/book")
async def create_book_transaction(transaction: BookTransactionSchema, db: Session = Depends(get_db)):
    # Agrega lógica adicional según tus necesidades, como verificar la disponibilidad del libro
    
    #BUSCAR EL LIBRO POR ID
    
    #VALIDAR LA EXISTENCIA DEL LIBRO SI EXISTE VALIDAR EL CAMPO ESTATUS SEA DIFERECTE DE PRESTADO PARA EJECUTAR Y SI NO MANDAR ERROR
    
    return crud.create_transaction(db, user_id=transaction.user_id, book_id=transaction.book_id, date_transaction=transaction.date_transaction, type_transaction=transaction.type_transaction)