from fastapi import FastAPI
from app.routers import predict_router

app = FastAPI(title="API Inmobiliaria Pro")

app.include_router(predict_router.router)

@app.get("/")
def health_check():
    return {
        "status":"ok",
        "mensaje":"API Inmobiliaria Pro está funcionando correctamente"
    }