from flask import Flask
from routes import user_routes

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Registrar las rutas definidas en user_routes
app.register_blueprint(user_routes)

# Entrada principal del programa
if __name__ == '__main__':
    app.run(debug=True)  # Iniciar la aplicación Flask en modo de depuración
