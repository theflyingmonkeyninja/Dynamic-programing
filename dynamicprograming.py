# -*- coding: utf-8 -*-
"""
Created on Sat march  8 22:31:08 2019

@author: dhananjay
"""

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1);
    
def fib(n):
    if (n == 2 or n ==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
    
def factdynp(n):
    memo ={};
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = n*factdynp(n-1);
        memo[n] = x ;
        
    return x
   

# def fib
       
#         
    

    
from timeit import default_timer as timer
from datetime import timedelta
start = timer()
factdynp(100)
end = timer()
print(timedelta(seconds=end-start))

start = timer()
fact(100)
end = timer()
print(timedelta(seconds=end-start))
