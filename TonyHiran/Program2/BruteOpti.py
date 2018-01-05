#!/usr/bin/env python3
import math
import numpy
import sys
print("\n____________________________________________________\n")
print("Welcome to the Brute Force 2-D Optimization Program!")
print("____________________________________________________\n")

print("Here are the common math symbols in Python:")
print("""
    add:          +
    subtract:     -
    multiply:     *
    divide:       /
    floor divide: //
    modulo:       %
    exponent:     **
    sqrt:         math.sqrt(expr)
    log:          math.log(x, base)
    sin:          math.sin(expr)
    cos:          math.cos(expr)
    tan:          math.tan(expr)
    e:            math.e
    π:            math.pi""")

print("____________________________________________________")

min_max=input("Choose desired outcome (min/max):")

#The program will try to minimize, but if min_max is max then it will min the negative of the obj
if(min_max == "max"):
    min_max = -1
elif(min_max == "min"):
    min_max = 1
else:
    print('invalid input')
    sys.exit(1)

obj = input("Enter Objective Function (eg. 'x**2+4*x*y+4*y**2'):\n")
x_lb = float(input("Enter x lower bound:"))
x_ub = float(input("Enter x upper bound:"))
x_inc = float(input("Enter x increment:"))
y_lb = float(input("Enter y lower bound:"))
y_ub = float(input("Enter y upper bound:"))
y_inc = float(input("Enter y increment:"))

# Read in constraints
new_line = None
print("Please enter constraints. Hit enter when done.")
constr = []
while new_line != '':
    new_line = input("Enter constraint (eg. x == y):")
    if(new_line != ''):
        constr.append(new_line)
print('Computing...')
#Initialize solution variables
x_sol = None
y_sol = None
obj_val = float('inf')

# Cycle through all x and y values
constr_val=None;
for x in numpy.linspace(x_lb, x_ub, 1 + (x_ub - x_lb)/x_inc): #arange was inaccurate when crossing zero
    for y in numpy.linspace(y_lb, y_ub, 1 + (y_ub - y_lb)/y_inc): #so used linspace instead which is theoretically equivalent
        constr_val = 1
        for i in range(0, len(constr)):
            constr_val *= eval(constr[i])
        if(min_max * eval(obj) < obj_val and constr_val == 1):
            obj_val = min_max * eval(obj) # negate the obj if 'max' was selected
            x_sol = x
            y_sol = y


obj_val = min_max * obj_val #un-negate the obj if max was selected
print("The optimal objective function value is %.4f" % obj_val )
print("At (x, y) = (", x_sol, ',', y_sol, ')')
