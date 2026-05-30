from fastapi import FastAPI
from pydantic import BaseModel, Field # Importamos al portero de la disco

app = FastAPI(
    title="API Inmobiliaria Inteligente",
    description="Esta es una API de ejemplo creada con FastAPI",
    version="1.0.0"
)
# Esquema de datos para la entrada de una casa, como si fuera el formulario que llenas para entrar a la disco, pero en este caso es para describir una casa. El portero (Pydantic) se asegura de que los datos sean correctos antes de dejarlos entrar a la fiesta (la función que maneja la lógica de la API).
class CasaInput(BaseModel):
    metros_cuadrados: float = Field(..., gt=10, description="Metros cuadrados de la casa, debe ser mayor a 10")
    habitaciones: int = Field(..., ge=1, le=15)
    tiene_garaje: bool
# Endpoint de ejemplo o punto de entrada
@app.get("/")
def mensaje_bienvenida():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}

# Creamos la ruta de prediccion
@app.post("/predecir")
def predecir_precio(datos_casa: CasaInput):
    # simulamos respuesta de prediccion
    precio_falso = datos_casa.metros_cuadrados * 1500
    return {
        "mensaje": "Datos recibidos correctamente",
        "casa_evaluada": datos_casa,
        "precio_estimado": precio_falso
    }