# Goods Shipment Marketplace

This project is a marketplace for goods shipment. It allows users to list items they want to ship and connect with shippers who can transport their goods.

## Features

* User registration and login
* Listing items for shipment
* Searching for shipments
* Bidding on shipments
* Payment integration
* Real-time tracking of shipments (future)

## Getting Started

(Instructions on how to set up and run the project will be added here later)

## Running the Application

1.  **Install dependencies:**
    Make sure you have Python and pip installed.
    Install Flask:
    ```bash
    pip install Flask
    ```
    (If you have a `requirements.txt` file, you can use `pip install -r requirements.txt` instead).

2.  **Run the Flask development server:**
    Navigate to the `goods_shipment_marketplace` directory (if you are in the root of the repo, `cd goods_shipment_marketplace`).
    Then run:
    ```bash
    python app/main.py
    ```
    The application will be running on `http://localhost:5000` (or `http://0.0.0.0:5000`).

## API Endpoints

### Authentication
*   `POST /register`
    *   Description: Registers a new user.
    *   Request Body (JSON): `{"username": "youruser", "password": "yourpassword", "email": "user@example.com"}`
    *   Response: Confirmation message and user ID.

### Shipments
*   `POST /shipments`
    *   Description: Creates a new shipment listing.
    *   Request Body (JSON): `{"user_id": 1, "description": "My valuable goods", "origin": "City A", "destination": "City B"}` (Get `user_id` from registration)
    *   Response: Confirmation message and shipment ID.
*   `GET /shipments`
    *   Description: Retrieves a list of all current shipments.
    *   Response: A JSON array of shipment objects.

## Running Tests
Navigate to the project's root directory (`goods_shipment_marketplace`) and run:
```bash
python -m unittest tests.test_app
```
Or, if `goods_shipment_marketplace` is your current directory:
```bash
python -m unittest discover tests
```
