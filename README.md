<h1 style="text-align: center;">BIBLIOTECA</h1>

Lo primero que vamos a hacer es crear un entorno virtual para instalar todas nuestras librerías.

<!-- Entorno Virtual -->
### haciendo uso de gitbash
python -m virtualenv venv
source venv/Script/activate

# Instalamos las Librerías Necesarias
pip install fastapi uvicorn sqlalchemy psycopg2 fastapi-utils python-multipart python-dotenv

# Ejecuta el servidor.
uvicorn entrypoint:app --reload
