from fastapi import APIRouter, HTTPException
from app.schemas import CasaInput
from app.ml_service import predictor_casas

router = APIRouter()
@router.post("/predecir", tags=["Predicciones"])
def endpoint_predecir(datos: CasaInput):
    try:
        precio = predictor_casas.predecir(
            datos.metros_cuadrados,
            datos.habitaciones,
            datos.tiene_garaje
        )
        return {
            "precio_estimado": round(precio, 2),
            "datos": datos
        }
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
        