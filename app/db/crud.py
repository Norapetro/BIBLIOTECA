from sqlalchemy.orm import Session # La sesión de la DB
from app.models.models import Book, User # El modelo ORM de nuestra DB
from app.schemas.schemas import BookSchema, UserSchema # el esquema del JSON

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
        title=book.title,
        author=book.author,
        publication_date=book.publication_date,
        publisher=book.publisher,
        num_pages=book.num_pages,
        description=book.description,
        price=book.price
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

def update_book(db: Session, book_id: int, updated_book_data: BookSchema):
    _book = get_book_by_id(db=db, book_id=book_id)       # Obtener el libro existente por su ID
    
    # Actualizar los campos del libro existente con los datos
    _book.title = updated_book_data.title
    _book.author = updated_book_data.author
    _book.publication_date = updated_book_data.publication_date
    _book.publisher = updated_book_data.publisher
    _book.num_pages = updated_book_data.num_pages
    _book.description = updated_book_data.description
    _book.price = updated_book_data.price
    
    db.commit()       # Guardar los cambios en la base de datos
    db.refresh(_book)     # Actualizar el objeto de libro en la sesión de base de datos 
    return _book

    
    
    
# Funciones CRUD para el modelo User

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserSchema):
    _user = User(
        cedula=user.cedula,
        username=user.username,
        email=user.email,
        phone=user.phone,
        address=user.address
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()
    return _user

def update_user(db: Session, user_id: int, username: str, email: str, phone: str, address: str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.username = username
    _user.email = email
    _user.phone = phone
    _user.address = address
    db.commit()
    db.refresh(_user)
    return _user