def show_menu():
    print("=== Menu ===")
    print("1. Greet")
    print("2. Exit")

def greet():
    print("Hello! You're doing great in Python!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            greet()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
