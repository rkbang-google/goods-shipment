from flask import Flask
from app.controllers.auth_controller import register_user_routes
from app.controllers.shipment_controller import register_shipment_routes

app = Flask(__name__)

# Register routes
register_user_routes(app)
register_shipment_routes(app)

if __name__ == '__main__':
    # Host 0.0.0.0 makes it accessible from outside the container if needed
    app.run(host='0.0.0.0', port=5000, debug=True)
