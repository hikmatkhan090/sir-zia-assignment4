from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Checks if the provided password (after hashing) matches the stored password hash for the given email.
    
    Parameters:
        email (str): The user's email address.
        stored_logins (dict): A dictionary mapping emails to hashed passwords.
        password_to_check (str): The password entered by the user.

    Returns:
        bool: True if login is successful, otherwise False.
    """
    hashed_input = hash_password(password_to_check)
    
    return stored_logins.get(email) == hashed_input


def hash_password(password):
    """
    Hashes a password using SHA256.

    Parameters:
        password (str): The plain-text password.

    Returns:
        str: The hashed version of the password.
    """
    return sha256(password.encode()).hexdigest()


def main():
    # Predefined email-password hash records
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"   # 123!456?789
    }

    print("🔐 Attempting login for example@gmail.com with password 'word':")
    print("✅ Success!" if login("example@gmail.com", stored_logins, "word") else "❌ Failed.")

    print("\n🔐 Attempting login for example@gmail.com with password 'password':")
    print("✅ Success!" if login("example@gmail.com", stored_logins, "password") else "❌ Failed.")

    print("\n🔐 Attempting login for code_in_placer@cip.org with password 'Karel':")
    print("✅ Success!" if login("code_in_placer@cip.org", stored_logins, "Karel") else "❌ Failed.")

    print("\n🔐 Attempting login for code_in_placer@cip.org with password 'karel':")
    print("✅ Success!" if login("code_in_placer@cip.org", stored_logins, "karel") else "❌ Failed.")

    print("\n🔐 Attempting login for student@stanford.edu with password 'password':")
    print("✅ Success!" if login("student@stanford.edu", stored_logins, "password") else "❌ Failed.")

    print("\n🔐 Attempting login for student@stanford.edu with password '123!456?789':")
    print("✅ Success!" if login("student@stanford.edu", stored_logins, "123!456?789") else "❌ Failed.")


if __name__ == '__main__':
    main()
