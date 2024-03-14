from fastapi import APIRouter, Depends
from app.db import crud
from app.schemas.schemas import PaymentSchema
from app.db.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/") 
async def create_payment(payment:  PaymentSchema, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)
