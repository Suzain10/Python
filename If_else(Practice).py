# -*- coding: utf-8 -*-
"""If_Else(Practice).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LgOPAcv1lhhKeLS_HafCEPIE6zRvTMOT
"""

num = int(input("Enter the value for num :  "))
if(num < 0):
  print("Number is negative")
elif(num == 0):
  print("Number is zero")
elif(num == 999):
  print("Number is largest 3 digit number")
else:
  print("Number is positive")

applePrice = int(input("Enter the price for apples: "))
 budget = int(input("Enter your budget: "))
 if (budget - applePrice > 150):
  print("You may buy some apples!")
elif (budget - applePrice < 50):
  print("You may buy 2 apples")
else:
  print("Don't buy anything now")

num = int(input("Enter the value for num :  "))
if(num < 0):
  print("Number is negative")
elif(num>0):
  if num > 0 and num <=10:
    print("Number lies betweeen 0 and 10")
  elif num >10 and num <=20:
    print("Number lies between 11 and 20")
  else:
    print("Number is positive")
else:
  print("Number is zero")

