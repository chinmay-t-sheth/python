# name_greeter.py

while True:
    name = input("Enter your name (or type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}!")
