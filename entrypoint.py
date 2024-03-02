from fastapi import FastAPI
import uvicorn
import app.models.models as model
from app.db.config import engine
from app.routes.routes import router as router_crud
from app.routes.users import router as user_router

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Details",
    description="Puede realizar operaciones CRUD utilizando esta API",
    version="1.0.0",
    docs_url="/docs",  # Agregar documentación de API
    redoc_url=None
)

@app.get("/")
def hello_world_check():
    return {
        "msg":"Hola, Este es el Sistema Bibliotecario."
    }

app.include_router(router=router_crud,tags=["Books CRUD"],prefix="/books")
app.include_router(router=user_router, tags=["Users CRUD"], prefix="/users")




if __name__ == "__main__":
    uvicorn.run("entrypoint:app",
                host="localhost",
                reload=True)