from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ruta de la base de datos 
DATABASE_URL = "sqlite:///books.db"

# Creamos el motor, el cual al comienzo de la ruta de la DB
# Se especifica que es sqlite
engine = create_engine(DATABASE_URL,
                    connect_args={"check_same_thread": False}
                    )

# Luego creamos los parametros para las sessiones que se creen de dicho motor
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# Creamos el mapeador ORM 
Base = declarative_base()

 # Creamos la función para el uso de session de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()