# This addition, subtraction, division, multiplication and modulus operations. 

from typing import Optional

from matplotlib.pyplot import cla


class Calculator:
    """This is a Python calculator that does addition, subtraction,
    division, multiplication and modulus operations.\n
    1. Multiplicaton -> | mul | M \n
    2. Addition -> | a | A \n
    3. Subtraction -> | s | S \n 
    4. Division -> | d | D \n
    5. Modulus -> | mod | Mod \n
     Please Enter the action you want to perform 
    """

    def __init__(self, action: str):
        self.action = action
        if self.action.casefold() in ('add', 'a', '2', 'addition'):
            return self.addition()

        elif self.action.casefold() in ('sub', 's', '3', 'subtraction', 'subtract'):
            return self.subtraction()

        
        elif self.action.casefold() in ('div', 'd', '4', 'division'):
            return self.division()

        
        elif self.action.casefold() in ('mul', 'multiply', '1', 'multiplication'):
            return self.multiplication()

        elif self.action.casefold() in ('mod','modulus', 5):
            return self.multiplication()
        
        else:
            print('Action does not exist')

    def addition(*args, **kwargs) -> Optional[float]:
        print("Enter first number: ", end ='')
        first_number = int(input())
        print()
        print("Enter Second number: ", end ='')
        second_number = int(input())

        print(f"{first_number} + {second_number} = {first_number+second_number}")

            
    def subtraction(*args, **kwargs) -> Optional[float]:
        
        print("Enter first number: ", end ='')
        first_number = int(input())
        print()
        print("Enter Second number: ", end ='')
        second_number = int(input())

        print(f"{first_number} - {second_number} = {first_number-second_number}")

    def division(*args, **kwargs):
        print("Enter first number: ", end ='')
        first_number = int(input())
        print()
        print("Enter Second number: ", end ='')
        second_number = int(input())

        print(f"{first_number} / {second_number} = {first_number/second_number}")

    def multiplication(*args, **kwargs):
        print("Enter first number: ", end ='')
        first_number = int(input())
        print()
        print("Enter Second number: ", end ='')
        second_number = int(input())

        print(f"{first_number} * {second_number} = {first_number*second_number}")

    def modulus(*args, **kwargs):
        print("Enter first number: ", end ='')
        first_number = int(input())
        print()
        print("Enter Second number: ", end ='')
        second_number = int(input())

        print(f"{first_number} mod(%) {second_number} = {first_number%second_number}")

print(Calculator.__doc__)
action = input()
calc = Calculator(action)
calc