from fastapi import FastAPI

app = FastAPI(
    title="Mi primera API con FastAPI",
    description="Esta es una API de ejemplo creada con FastAPI",
    version="1.0.0"
)

# Endpoint de ejemplo o punto de entrada
@app.get("/")
def mensaje_bienvenida():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}