from sqlalchemy.orm import Session # La sesión de la DB
from app.models.models import Book # El modelo ORM de nuestra DB
from app.schemas.schemas import BookSchema # el esquema del JSON

# creamos la función para obtener todos los libros
def get_book(db:Session, skip:int=0, limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all()
# query busca segun nuestro modelo
# skip es el salto o pasos que hace
# limit es la cantidad total de resultados que trae
# la función all trae todos los resultados 

def get_book_by_id(db:Session,book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()
# buscamos los resultados del modelo 
# pero hacemos un filtro por el id
# obtenemos el primer resultado

def create_book(db:Session, book:BookSchema):
    _book = Book(
        title = book.title,
        description = book.description
    )
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book
# creamos le damos las propiedades 
# asignando cada valor correspondiente del JSON al Modelo
# guardamos en la DB

def remove_book(db:Session, book_id:int):
    _book = get_book_by_id(db=db,book_id=book_id)
    db.delete(_book)
    db.commit()
    return _book
# para eliminar filtramos por el Id
# eliminamos

def update_book(db:Session, book_id:int,
                title:str, description:str):
    _book = get_book_by_id(db=db, book_id=book_id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book
    # filtramos por id 
    # reasignamos los valores de la entidad del modelo
    # guardamos los cambios en la DB