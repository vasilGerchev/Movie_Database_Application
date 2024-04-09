import hashlib

# Dummy database of users
users = {
    "user1": "password1",
    "user2": "password2"
}


def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(username, password):
    """Authenticate the user."""
    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        return True
    else:
        return False


def get_logged_user():
    """Return the currently logged-in user."""
    # For demonstration purposes, return a hardcoded user
    return "user1"  # You may replace this with your actual login implementation
