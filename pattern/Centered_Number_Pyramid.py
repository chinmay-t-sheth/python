rows = 5
for i in range(1, rows + 1):
    # 1. print spaces
    for j in range(rows - i):
        print(" ", end="")
    # 2. print numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

/*

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

*/
