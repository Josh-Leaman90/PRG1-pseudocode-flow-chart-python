STORED_PASSWORD = "python123"

for attempt in range(3):
    password = input("Enter your password: ")

    if password == STORED_PASSWORD:
        print("Password correct. You are logged in.")
        break
    else:
        if attempt < 2:
            print("Password is wrong. You have", 2 - attempt, "more attempts.")
        else:
            print("You are locked out. No more attempts are allowed.")
