# Step 1: Store correct credentials
correct_username = "admin"
correct_password = "1234"

# Step 2: Take input from user
user_username = input("Enter username: ")
user_password = input("Enter password: ")

# Step 3: Validate
if user_username == correct_username and user_password == correct_password:
    print("Login Successful ✅")
elif user_username != correct_username:
    print("Username is incorrect ❌")
elif user_password != correct_password:
    print("Password is incorrect ❌")
