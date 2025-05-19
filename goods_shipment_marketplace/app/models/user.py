class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # In a real app, this should be hashed
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"
