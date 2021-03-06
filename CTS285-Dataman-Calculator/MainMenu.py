# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:29:20 2021

@author: mput7
"""
import MemoryBank as MB
import NumberGuesser as NG
import AnswerChecker as AC
import MissingNumber as MN
import Tournament as TO
import ElectroFlash as EF
import NormalCalc as NC
def main():
    loop = True
    while loop == True:
        try:
            menu = int(input("""
____________________________________________________
  _____       _______       __  __          _   _ 
 |  __ \   /\|__   __|/\   |  \/  |   /\   | \ | |
 | |  | | /  \  | |  /  \  | \  / |  /  \  |  \| |
 | |  | |/ /\ \ | | / /\ \ | |\/| | / /\ \ | . ` |
 | |__| / ____ \| |/ ____ \| |  | |/ ____ \| |\  |
 |_____/_/    \_\_/_/    \_\_|  |_/_/    \_\_| \_|                                                
____________________________________________________
                                                 
1. Answer Checker
2. Number Guesser
3. Memory Bank
4. Missing Number
5. Tournament
6. Electro Flash
7. Normal Calculator
8. Quit
> """))

            if menu == 1:
                AC.ansChk()
            elif menu == 2:
                NG.numGuess()
            elif menu == 3:
                MB.memBank()
            elif menu == 4:
                MN.missNum()
            elif menu == 5:
                TO.tournament()
            elif menu == 6:
                EF.electroFlash()
            elif menu == 7:
                NC.normalCalc()
            elif menu == 8:
                loop = False
            else:
                print("Please use a number listed on the menu")
        except ValueError:
            print("Please enter a value")
        
main()

print("Goodbye.")