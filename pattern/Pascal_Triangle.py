def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def pascal_triangle(n):
    for i in range(n):
        # print spaces
        print(" " * (n - i), end="")
        for j in range(i + 1):
            val = factorial(i) // (factorial(j) * factorial(i - j))
            print(val, end=" ")
        print()

# Example: 5 rows
pascal_triangle(5)

/*
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
*/
