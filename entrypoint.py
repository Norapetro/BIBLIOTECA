from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import app.models.models as model
from app.db.config import SessionLocal, engine
from app.routes.routes import router as router_crud
from app.routes.users import router as user_router
from app.routes.transacción import router as transaction_router
from app.routes.paymentBook import router as payment_router


model.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173/"
]

app = FastAPI(
    title="Book Details",
    description="You can perform CRUD operations using this API",
    version="1.0.0",
    docs_url="/docs",  # Agregar documentación de API
    redoc_url=None
)

@app.get("/")
def hello_world_check():
    return {
        "msg":"Hola, Biblioteca BACKEND ."
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Reemplaza con el origen de tu aplicación React
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(router=router_crud,tags=["Books CRUD"],prefix="/books")
app.include_router(router=user_router, tags=["Users CRUD"], prefix="/users")
app.include_router(router=transaction_router, tags=["transaction CRUD"], prefix="/transaction")
app.include_router(router=payment_router,tags=["payment CRUD"], prefix="/payment")




if __name__ == "__main__":
    uvicorn.run("entrypoint:app",
                host="localhost",
                reload=True)