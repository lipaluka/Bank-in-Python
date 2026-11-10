import func

def mainMenu():
    print("0)Register\n"
        "1)User Login\n" \
            "2)Info\n" \
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
            print("===================================")
            loggedInMenu(username)
        else:
            print("Invalid username or password.")

    elif userInput == "2":
        print("Information:")
        print("This is a simple banking application where you can register, log in, and manage your account.")
        print("You can perform operations like checking your balance, depositing money, and withdrawing money.")
        print("Please make sure to keep your username and password secure.")
        print("For any issues or inquiries, please contact support")
        print("Thank you for using our banking application!")
        print("Version: In-Development...")
    elif userInput == "3":
        print("Exiting the application. Goodbye!")
        exit()
    else:
        print("Invalid input. Please try again.")
        mainMenu() 

def loggedInMenu(username):          
    while True:
        userInput = input("Select operation:\n"
                          "0)Check Balance\n"
                          "1)Deposit Money\n"
                          "2)Withdraw Money\n"
                          "3)Logout\n")
        

        if userInput == "3":
            print("Logging out...")
            break                    
        else:
            print("Invalid input...")   
            