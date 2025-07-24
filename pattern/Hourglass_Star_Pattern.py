rows = 5

# Inverted pyramid
for i in range(rows): # starts from 0 to 4
    print(" " * i + "*" * (2*(rows - i) - 1))

# Normal pyramid
for i in range(1, rows):
    print(" " * (rows - i - 1) + "*" * (2*i + 1))

/*
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
*/
