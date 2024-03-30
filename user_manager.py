class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user

    def authenticate_user(self, username, password):
        if username in self.users:
            return self.users[username].authenticate(username, password)
        return False
