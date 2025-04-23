def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")
    
    return first_name, last_name, email_address


def main():
    user_data = get_user_info()
    print("\nReceived the following user data:")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")
    print(f"Email Address: {user_data[2]}")


if __name__ == "__main__":
    main()
