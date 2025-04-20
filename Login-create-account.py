# user_auth.py

# Temporary user database (in-memory dictionary)
user_database = {}

def create_account(username, password):
    """
    Creates a new user if the username doesn't exist already.
    """
    if username in user_database:
        return "Username already taken."
    user_database[username] = password
    return " Account successfully created!"

def login(username, password):
    """
    Verifies login credentials.
    """
    if username not in user_database:
        return "Username not found."
    if user_database[username] != password:
        return "Incorrect password."
    return "Login successful!"

# Example usage
if __name__ == "__main__":
    print(create_account("luzie", "mypassword"))      # Should succeed
    print(create_account("luzie", "newpass"))         # Should fail (username taken)
    print(login("luzie", "mypassword"))               # Should succeed
    print(login("luzie", "wrongpassword"))            # Should fail
    print(login("unknownuser", "pass"))               # Should fail

