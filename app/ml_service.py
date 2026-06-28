import joblib

class HousePricePredictor:
    def __init__(self):
        try:
            self.model = joblib.load("modelos_ia/modelo_casas.joblib")
        except Exception:
            self.model = None
    def predecir(self, metros, habitaciones, garaje):
        if not self.model:
            raise ValueError("Modelo no cargado")
        datos = [[metros, habitaciones, garaje]]
        return self.model.predict(datos)[0]
predictor_casas = HousePricePredictor()
