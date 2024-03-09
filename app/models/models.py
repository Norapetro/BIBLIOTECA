from sqlalchemy import Column, Integer, String, Date, Float, Enum, ForeignKey, Date
from app.db.config import Base
from app.utils.utils import StateBook
# Definición de la clase para representar un libro en la base de datos
class Book(Base):
    """
    Clase para representar un libro en la base de datos.
    """
    __tablename__ = "book"
    
    # Columnas de la tabla 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)  # Título del libro (no puede ser nulo)
    author = Column(String)  # Nombre del autor
    publication_date = Column(Date)  # Fecha de publicación
    publisher = Column(String)  # Editorial
    num_pages = Column(Integer)  # Número de páginas
    description = Column(String)  # Descripción opcional del libro
    price = Column(Float)  # Precio
    state = Column(Enum(StateBook), default=StateBook.ASSET)
    
# Definición de la clase para representar un usuario en la base de datos
class User(Base):
    """
    Clase para representar un usuario en la base de datos.
    """
    __tablename__ = "user"
    
    # Columnas de la tabla 'user'
    id = Column(Integer, primary_key=True)
    cedula = Column(String, unique=True)  # Número de cédula del usuario
    username = Column(String, nullable=False, unique=True)  # Nombre de usuario único
    email = Column(String, nullable=False, unique=True)  # Correo electrónico único
    phone = Column(String, nullable=False, unique=True)  # Teléfono del usuario
    address = Column(String)  # Dirección del usuario

class BookTransaction(Base):
    __tablename__ = "book_transaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    date_transaction = Column(Date)
    type_transaction = Column(String)

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def mostrar_catalogo(self):
        print("Catálogo de la biblioteca:")
        for libro in self.catalogo:
            print(libro)