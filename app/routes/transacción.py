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
    if transaction.type_transaction == "prestamo" and book.state == StateBook.ACTIVE:
        state = "BORROWED"
    elif transaction.type_transaction == "devolucion" and book.state == StateBook.BORROWED:
        state = "ACTIVE"
    else: 
        return Response(
            status="bad request",
            code="400",
            message="transaction invalid"
        )
                
    
    crud.update_book(db, book_id=book.id, title=book.title, author=book.author, publication_date=book.publication_date,
                          publisher=book.publisher,num_pages=book.num_pages,description=book.description,price=book.price,state=state)
         
    return crud.create_transaction(
         db, user_id=transaction.user_id, 
         book_id=transaction.book_id, 
         date_transaction=transaction.date_transaction, 
         type_transaction=transaction.type_transaction
        )
    