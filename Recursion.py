# -*- coding: utf-8 -*-
"""Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CLSKJOF8pieVjgnbe_ABr1QiGhC7ePEz
"""

#Fibonacci Series Using Recursion:
def fiboo(n):
  if(n==0 or n==1 or n==2 ):  #checkk
    return 1
  else:
   return fiboo(n-1) + fiboo(n-2)
print(fiboo(9))

#Factorial Using Recursion:
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * factorial (n-1)

print(factorial(3))