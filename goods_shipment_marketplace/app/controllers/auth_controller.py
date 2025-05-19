from flask import Flask, request, jsonify
from app.models import User

# In-memory user storage for simplicity
users = []
next_user_id = 1

def register_user_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        global next_user_id
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password or not email:
            return jsonify({'message': 'Missing username, password, or email'}), 400

        if any(user.username == username for user in users):
            return jsonify({'message': 'Username already exists'}), 409

        new_user = User(username=username, password=password, email=email)
        # In a real app, you would assign a unique ID from a database
        setattr(new_user, 'id', next_user_id)
        users.append(new_user)
        next_user_id += 1
        
        return jsonify({'message': 'User registered successfully', 'user_id': new_user.id}), 201

# Helper function to get users (for testing/debugging)
def get_all_users():
    return users
