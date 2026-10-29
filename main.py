import func


print("0)Register\n"
      "1)User Login\n" \
        "2)Bank Login\n" \
        "3)Exit\n")


userInput = input("Select operation: ")

if userInput == "0":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if func.register(func.loadFromJson(), username, password):
        print("Registration successful! You can now log in.")
    else:
        print("Username already exists. Please try again.")

elif userInput == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if func.login(func.loadFromJson(), username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

elif userInput == "2":
    






