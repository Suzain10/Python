# -*- coding: utf-8 -*-
"""Sum of n numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IwSS7Nwm93fKdzmi1ELETgaaeRtRbb_1
"""

#Program to calculate sum of first n numbers:
def num(n):
  sum = n*(n+1)/2
  return sum
num(10)

#Taking input from the user:
def num(n):
    return n*(n+1)/2

user_input = int(input("Enter a number: "))
result = num(user_input)
print("The sum of numbers from 1 to", user_input, "is:", result)