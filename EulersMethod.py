import math 
import numpy as np 
import scipy as sp
import pandas as pd 
import matplotlib.pyplot as plt 


# Section 1.4 Problem 5
a=1
h=0.1

def f(x,y): 
    return x-y**2 

def Euler(): 
    x=1 
    y=0
    print("Iter \t x \t y \n")
    for i in range(6): 
        print(i,"\t",x,"\t",y,"\n")
        y=y+f(x,y)*h
        x+=h
        

Euler()

#Here are some more functions you can try. Just copy the function and paste 
# them in the code block under the function 
#   def f(x,y) =dy/dx. 
# You can adjust the step size, h = 0.1 or 0.2 or 0.05, and the initial conditions 
# as you see fit.  
'''
Example Functions
f(x,y) = -x/y, y(0)= 4
f(x,y)=y(2-y), y(0)=3
f(x,y) = x-y**2, y(1) = 0 
'''