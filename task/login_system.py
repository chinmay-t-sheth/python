attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "1234":
        print("✅ Login Successful!")
        break
    else:
        print("❌ Wrong credentials. Try again.")
        attempts += 1

if attempts == 3:
    print("🚫 Access Denied.")
