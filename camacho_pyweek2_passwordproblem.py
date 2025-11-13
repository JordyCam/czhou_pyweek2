# Get user's age
age = int(input("Enter your age: "))

# Check age condition
if age > 20:
    print("Access granted.")
else:
    # Ask for password if age is 20 or less
    password = input("Enter password: ")
    if password == "12345":
        print("Access granted.")
    else:
        print("Error.")