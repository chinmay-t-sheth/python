def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
terms = int(input("How many terms? "))
generate_fibonacci(terms)
