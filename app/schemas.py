from pydantic import BaseModel, Field

# guardamos todas las reglas de validacion
class CasaInput(BaseModel):
    metros_cuadrados: float = Field(..., gt=10)
    habitaciones: int = Field(..., ge=1, le=15)
    tiene_garaje:int = Field(...)
    