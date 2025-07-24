rows = int(input("Enter number of rows: "))

a, b = 0, 1
for i in range(1, rows + 1):
    for j in range(i):
        print(a, end=" ")
        a, b = b, a + b
    print()

/*
0
1 1
2 3 5
8 13 21 34
55 89 144 233 377
*/
