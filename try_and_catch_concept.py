while True:

    inp = int(input("Operation (press 2 to quit): "))

    if inp == 1:
        
        try:
            print("Addition")
            a = int(input("1st Number: "))
            b = int(input("2nd Number: "))
            print(a+b)
        
        except:
            print("IO")
    
    elif inp == 2:
        break
    
    else:
        print("Invalid Operation")