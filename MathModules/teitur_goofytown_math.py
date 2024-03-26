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

#Nothing set in stone, :stars_in_eyes:

def Add(x,y,GoofyTown=False):
    if not GoofyTown:
        return x+y
    else:
        theresult = x+y
        return theresult

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
