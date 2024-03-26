"""
Louie

Functions:
    Add(x,y)
    Subtract(x,y)
    Multiply(x,y)
    Divide(x,y)
    Modulus(x,y)
    Quotient(x,y)
    Exponent(x,y)
"""
"""Nothing set in stone, :stars_in_eyes:"""

import random # An included library with Python install. 
from tkinter import messagebox as mb  

def Add(x,y,GoofyTown=False) -> int:
    if not GoofyTown:
        return x+y
    else:
        guess = random.randint(x,(x+y)*2)
        while(mb.askyesno('Uhhhhhhh', f'{x} + {y} = {guess} {"?"*random.randint(1,13)}') != True):
            guess = random.randint(x,(x+y)*2)
        return guess

def Subtract(x,y,GoofyTown=False):
    return x-y

def Multiply(x,y,GoofyTown=False):
    return x*y

def Divide(x,y,GoofyTown=False):
    return x/y

def Modulus(x,y,GoofyTown=False):
    return x%y

def Quotient(x,y,GoofyTown=False):
    return x//y

def Exponent(x,y,GoofyTown=False):
    return x**y

if __name__ == "__main__":
    print("Testing, Testing, 123")
    print(Add(7,1,True))