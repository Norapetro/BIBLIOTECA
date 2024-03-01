from sqlalchemy import Column, Integer, String
from app.db.config import Base

# clase 
class Book(Base):
    # nombre de la tabla
    __tablename__ = "book"
    
    # Las columnas de nuestra tabla y el tipo de dato de cada una
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)    