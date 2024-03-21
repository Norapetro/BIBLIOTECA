from fastapi import APIRouter, Depends
from app.db import crud
from app.schemas.schemas import BookTransactionSchema, Response
from app.db.config import get_db
from sqlalchemy.orm import Session

from app.utils.utils import StateBook

router = APIRouter()

@router.post("/book")
async def create_book_transaction(transaction: BookTransactionSchema, db: Session = Depends(get_db)):
    
    #BUSCAR EL LIBRO POR ID
    book = crud.get_book_by_id(db, transaction.book_id)
    print(transaction.type_transaction)
    if transaction.type_transaction == "prestamo":
        if book.state == StateBook.BORROWED:
            return Response(
                status="bad request",
                code="400",
                message="El libro ya está préstado y no se puede prestar nuevamente hasta que sea devuelto."
            )
        else:
            state = StateBook.BORROWED
    elif transaction.type_transaction == "devolucion":
        if book.state != StateBook.BORROWED:
            return Response(
                status="bad request",
                code="400",
                message="El libro no está en préstado y, por lo tanto, no se puede devolver."
            )
        else:
            state = StateBook.ACTIVE
    else: 
        return Response(
            status="bad request",
            code="400",
            message="transaction invalid"
        )
                
    # Actualizar el estado del libro
    crud.update_book(db, book_id=book.id, title=book.title, author=book.author, publication_date=book.publication_date,
                          publisher=book.publisher,num_pages=book.num_pages,tematica=book.tematica,price=book.price,state=state)
         
    return crud.create_transaction(db, 
         user_id=transaction.user_id, 
         username=transaction.username,
         book_id=transaction.book_id, 
         book_title=transaction.book_title,
         date_transaction=transaction.date_transaction, 
         type_transaction=transaction.type_transaction
        )
    