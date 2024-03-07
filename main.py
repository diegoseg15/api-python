from flask import Flask, jsonify, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta raíz de la API
@app.route('/')
def root():
    return "Hola mundo"  # Devuelve un mensaje simple cuando se accede a la ruta raíz

# Ruta para obtener información de un usuario específico
@app.route("/users/<user_id>")
def get_user(user_id):
    # Datos ficticios del usuario
    user = {'id': user_id, 'name': 'test', 'telefono': '0987654321'}
    
    # Verificar si se proporcionó un parámetro de consulta en la URL
    query = request.args.get('query')
    if query:
        user['query'] = query  # Agregar el parámetro de consulta al objeto de usuario si existe
    
    # Devolver los datos del usuario en formato JSON
    return jsonify(user), 200

# Ruta para crear un nuevo usuario
@app.route("/users", methods=['POST'])
def create_user():
    # Obtener los datos enviados en la solicitud POST
    data = request.get_json()
    data['status'] = 'user created'  # Agregar un campo adicional para indicar el estado de la creación del usuario
    
    # Devolver los datos del usuario recién creado junto con un código de estado 201 (CREATED)
    return jsonify(data), 201

# Ruta para actualizar información de un usuario específico (PUT)
@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    # Obtener los datos enviados en la solicitud PUT
    data = request.get_json()
    
    # Aquí puedes implementar la lógica para actualizar los detalles del usuario en tu sistema
    
    # Por ahora, solo se devolverá un mensaje de éxito junto con el ID del usuario actualizado
    return jsonify({'message': 'User updated successfully', 'user_id': user_id}), 200

# Ruta para eliminar un usuario específico (DELETE)
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    # Aquí puedes implementar la lógica para eliminar el usuario con el ID proporcionado de tu sistema
    # Por ahora, solo se devolverá un mensaje de éxito
    return jsonify({'message': 'User deleted successfully', 'user_id': user_id}), 200

# Entrada principal del programa
if __name__ == '__main__':
    app.run(debug=True)  # Iniciar la aplicación Flask en modo de depuración
