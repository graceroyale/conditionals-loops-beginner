# This line of code prompts the user to keep trying until they enter the right password.
user_name = input("Enter your username: ")
password = "python123"
user_input = ""
while user_input != password:
    user_input = input("Enter the password: ")
    if user_input == password:
        print(f"Access granted. Welcome {user_name}!")
    else:
        print(f"Incorrect password, {user_name}. Please try again.")
