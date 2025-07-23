def left_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def right_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# --- Main Menu ---
while True:
    print("\n🌟 STAR PATTERN GENERATOR 🌟")
    print("1. Left-Aligned Triangle")
    print("2. Right-Aligned Triangle")
    print("3. Centered Pyramid")
    print("4. Inverted Centered Pyramid")
    print("5. Exit")

    choice = input("Choose pattern (1-5): ")

    if choice == "5":
        print("Thanks for using the tool. Bye!")
        break

    rows = int(input("Enter number of rows: "))

    if choice == "1":
        left_triangle(rows)
    elif choice == "2":
        right_triangle(rows)
    elif choice == "3":
        pyramid(rows)
    elif choice == "4":
        inverted_pyramid(rows)
    else:
        print("Invalid choice. Try again.")
