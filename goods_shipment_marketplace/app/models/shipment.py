class Shipment:
    def __init__(self, user_id, description, origin, destination, status="pending"):
        self.user_id = user_id  # ID of the user who created the shipment
        self.description = description
        self.origin = origin
        self.destination = destination
        self.status = status  # e.g., pending, in_transit, delivered

    def __repr__(self):
        return f"<Shipment {self.description[:20]}>"
