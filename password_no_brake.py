STORED_PASSSWORD = "python123"
logged_in = False

for attempt in range(3):
    password = input("Enter your password: ")

    if password == STORED_PASSSWORD:
        logged_in = True
        print("Password correct. You are logged in.")
    else:
        if attempt < 2:
            print("Password is wrong. You have", 2 - attempt, "more attempts.")
        else:
            print("You are locked out. No more attempts are allowed.")

print("Program finished.")
