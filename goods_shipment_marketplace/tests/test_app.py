import unittest
import json
from app.main import app # Import the Flask app instance
from app.models import User, Shipment

# Reset in-memory data stores for each test run for isolation
# This is a bit of a hack for in-memory data.
# In a real app with a database, you'd use a test database.
from app.controllers import auth_controller, shipment_controller

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset data before each test
        auth_controller.users = []
        auth_controller.next_user_id = 1
        shipment_controller.shipments = []
        shipment_controller.next_shipment_id = 1

    def test_01_register_user(self):
        payload = {
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
        response = self.app.post('/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User registered successfully')
        self.assertEqual(data['user_id'], 1)
        # Check if user was actually added
        self.assertEqual(len(auth_controller.get_all_users()), 1)
        self.assertEqual(auth_controller.get_all_users()[0].username, "testuser")

    def test_02_register_user_missing_fields(self):
        payload = {"username": "testuser2"} # Missing password and email
        response = self.app.post('/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Missing username, password, or email')

    def test_03_register_user_duplicate_username(self):
        payload = {
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
        self.app.post('/register', data=json.dumps(payload), content_type='application/json') # First registration
        response = self.app.post('/register', data=json.dumps(payload), content_type='application/json') # Duplicate
        self.assertEqual(response.status_code, 409)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Username already exists')

    def test_04_create_shipment(self):
        # First, register a user
        user_payload = {
            "username": "shipper",
            "password": "password123",
            "email": "shipper@example.com"
        }
        user_response = self.app.post('/register', data=json.dumps(user_payload), content_type='application/json')
        user_id = json.loads(user_response.data)['user_id']

        shipment_payload = {
            "user_id": user_id,
            "description": "Test shipment",
            "origin": "City A",
            "destination": "City B"
        }
        response = self.app.post('/shipments', data=json.dumps(shipment_payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Shipment created successfully')
        self.assertEqual(data['shipment_id'], 1)
         # Check if shipment was actually added
        self.assertEqual(len(shipment_controller.get_all_shipments()), 1)
        self.assertEqual(shipment_controller.get_all_shipments()[0].description, "Test shipment")


    def test_05_create_shipment_missing_fields(self):
        shipment_payload = {"description": "Test shipment"} # Missing user_id, origin, destination
        response = self.app.post('/shipments', data=json.dumps(shipment_payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Missing required shipment data')

    def test_06_get_shipments(self):
        # Register a user and create a shipment first
        user_payload = {"username": "lister", "password": "secure", "email": "lister@test.com"}
        user_resp = self.app.post('/register', data=json.dumps(user_payload), content_type='application/json')
        user_id = json.loads(user_resp.data)['user_id']
        
        shipment_payload1 = {"user_id": user_id, "description": "Books", "origin": "Warehouse", "destination": "Bookstore"}
        self.app.post('/shipments', data=json.dumps(shipment_payload1), content_type='application/json')
        
        shipment_payload2 = {"user_id": user_id, "description": "Electronics", "origin": "Factory", "destination": "Retail"}
        self.app.post('/shipments', data=json.dumps(shipment_payload2), content_type='application/json')

        response = self.app.get('/shipments')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['description'], "Books")
        self.assertEqual(data[1]['description'], "Electronics")

if __name__ == '__main__':
    unittest.main()
