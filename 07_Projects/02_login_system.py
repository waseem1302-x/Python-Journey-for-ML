import os

# 🔐 File to store user credentials
CREDENTIAL_FILE = "users.txt"

# ✅ Function to register a new user
def register():
    print("\n📝 Register New User")
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()

    if not username or not password:
        print("❌ Username or password can't be empty.")
        return

    # Check if username already exists
    if os.path.exists(CREDENTIAL_FILE):
        with open(CREDENTIAL_FILE, "r") as file:
            for line in file:
                stored_user, _ = line.strip().split(",")
                if username == stored_user:
                    print("⚠️ Username already exists. Try logging in.")
                    return

    # Save new user
    with open(CREDENTIAL_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    print("✅ Registration successful! You can now log in.\n")

# 🔓 Function to login
def login():
    print("\n🔑 Login")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not os.path.exists(CREDENTIAL_FILE):
        print("🚫 No users registered yet.")
        return

    with open(CREDENTIAL_FILE, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if username == stored_user and password == stored_pass:
                print(f"\n✅ Welcome back, {username}!")
                return
    print("❌ Incorrect username or password.")

# 📋 Main menu
def main():
    while True:
        print("\n=== LOGIN SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# 🚀 Start the app
main()
