
import random as rand
def electroFlash():
    randomizer1 = 1
    randomizer2 = 1
    try:
        difficulty = int(input("Input a number from 1-9 to select how\nmany problems you want to do\n> "))
        operator = int(input("""
1. Additon
2. Subtraction
3. Multiplication
> 
"""))

        for i in range(difficulty):
            randomizer1 += rand.randint(5, 20)
            randomizer2 += rand.randint(5, 20)
            num1 = rand.randint(5, randomizer1)
            num2 = rand.randint(5, randomizer2)
            if operator == 1:
                ans = num1 + num2
                print(num1,"+",num2,"=")
                userAns = int(input("Input the answer to this question:"))
            elif operator == 2:
                ans = num1 - num2    
                print(num1,"-",num2,"=")
                userAns = int(input("Input the answer to this question:"))
            elif operator == 3:
                ans = num1 * num2
                print(num1,"*",num2,"=")
                userAns = int(input("Input the answer to this question:"))
            else:
                print("Error")
                
            if userAns == ans:
                print("Correct!\n")
            else:
                print("Wrong\n")
    except ValueError:
        print("Please enter a value")
        electroFlash()    

    