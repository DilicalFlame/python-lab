# A simple while loop that keeps asking for a password until the user enters the correct one

def password_validator():
    correct_password = "secure123"
    while True:
        user_input = input("Enter the password: ")
        if user_input == correct_password:
            print("Access granted.")
            break
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    password_validator()