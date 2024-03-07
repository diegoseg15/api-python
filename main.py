from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return "Hola mundo" 

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {'id': user_id, 'name': 'test', 'telefono': '0987654321'}
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

@app.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    data['status'] = 'user created'
    return jsonify(data), 201

@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify({'message': 'User updated successfully', 'user_id': user_id}), 200

if __name__ == '__main__':
    app.run(debug=True)
