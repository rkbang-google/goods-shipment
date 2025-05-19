from flask import request, jsonify
from app.models import Shipment
# Assuming users are managed by auth_controller and we can get user_id after authentication
# For now, we'll pass user_id in the request for simplicity

# In-memory shipment storage
shipments = []
next_shipment_id = 1

def register_shipment_routes(app):
    @app.route('/shipments', methods=['POST'])
    def create_shipment():
        global next_shipment_id
        data = request.get_json()
        user_id = data.get('user_id') # In a real app, get this from session/token
        description = data.get('description')
        origin = data.get('origin')
        destination = data.get('destination')

        if not all([user_id, description, origin, destination]):
            return jsonify({'message': 'Missing required shipment data'}), 400

        # In a real app, you'd verify the user_id exists
        # from app.controllers.auth_controller import get_all_users
        # if not any(user.id == user_id for user in get_all_users()):
        #     return jsonify({'message': 'User not found'}), 404


        new_shipment = Shipment(user_id=user_id, description=description, origin=origin, destination=destination)
        setattr(new_shipment, 'id', next_shipment_id)
        shipments.append(new_shipment)
        next_shipment_id += 1
        
        return jsonify({'message': 'Shipment created successfully', 'shipment_id': new_shipment.id}), 201

    @app.route('/shipments', methods=['GET'])
    def get_shipments():
        # Convert shipment objects to dictionaries for JSON serialization
        shipments_data = []
        for shipment in shipments:
            shipments_data.append({
                'id': shipment.id,
                'user_id': shipment.user_id,
                'description': shipment.description,
                'origin': shipment.origin,
                'destination': shipment.destination,
                'status': shipment.status
            })
        return jsonify(shipments_data), 200

# Helper function to get shipments (for testing/debugging)
def get_all_shipments():
    return shipments
