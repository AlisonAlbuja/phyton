from flask import Flask
import os

app = Flask(__phyton__)

@app.route("/")
def hello_world():
    return "Hello Alison Abigail "

if __phyton__ == "__main__":
    # Heroku asigna dinámicamente el puerto a través de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto de Heroku o 5000 por defecto
    app.run(host="0.0.0.0", port=port)  # Hace que la app sea accesible en cualquier dirección
