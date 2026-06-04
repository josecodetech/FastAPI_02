from sklearn.ensemble import RandomForestRegressor
import os
import joblib
print("--- Preparando los datos de prueba ---")
X_entrenamiento = [
[120,3,1],
[80,2,0],
[150,4,1],
[60,1,0]
]
y_entrenamiento = [180000, 120000, 250000, 90000]
print("--- Entrenando el modelo ---")
modelo = RandomForestRegressor(n_estimators=10, random_state=42)
modelo.fit(X_entrenamiento, y_entrenamiento)
print("--- Guardando el modelo entrenado ---")
os.makedirs("modelos", exist_ok=True)
ruta_archivo = "modelos/modelo_casas.joblib"
joblib.dump(modelo, ruta_archivo)
print(f"Modelo guardado en: {ruta_archivo}")