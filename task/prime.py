import math

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
