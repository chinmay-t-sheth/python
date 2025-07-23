while True:
    print("\n select ")
    print("1.add ")
    print("2.sub ")
    print("3.mul ")
    print("4.exit ")
    
    choice= input("enter ur choice ")
    
    if choice=='4':
        print("bye")
        break
    
    if choice not in ['1','2','3']:
        print("invalid")
        continue
    
    a=int(input("enter your first number: "))
    b=int(input("enter your second number: "))
    
    if choice=='1':
        print(a+b)
    if choice=='2':
        print(a-b)
    if choice=='3':
        print(a*b)

    
    
    
    
    
    
    
    
    
    
    
    
