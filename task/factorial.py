def factorial(n):
    """Returns factorial of a given non-negative integer"""
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Main program
try:
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is:", factorial(num))
except ValueError:
    print("Please enter a valid integer.")
