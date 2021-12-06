








def normalCalc():
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        menu = int(input("""
What operation do you  want to use?
1. Addition
2. Subtraction
3. Multiplication
4. Division
> """))
        if menu == 1:
            ans = num1 + num2
            print(ans,"=",num1,"+",num2)
        elif menu == 2:
            ans = num1 - num2
            print(ans,"=",num1,"-",num2)
        elif menu == 3:
            ans = num1 * num2
            print(ans,"=",num1,"*",num2)
        elif menu == 4:
            ans = num1 / num2
            print(ans,"=",num1,"/",num2)
        else:
            print("Please use a number listed on the menu")
            
    except ValueError:
        print("Please enter a value")
        