# -*- coding: utf-8 -*-
"""Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11tLjYPRYuYhJ2CLh7gOFWP5_lT61u8BV
"""

#Functions:Block of code that performs specific task whenever it is called.Better to use functions to make your task easier.
#Built in Func:are defined and pre coded. & User Defined:created as per need using def keyword.

a = 9
b = 8
gmean = (a*b)/(a+b)
print(gmean)

def function_name(parameters):
  pass

#Calling a Func:
def name(fname,lname):
  print("Hello",fname,lname)
  #print(input())
  print(fname,lname)
name("Sam","Wilson")

def calculateGmean(a,b):
 mean = (a*b)/(a+b)
 print(mean)

def isGreater(a,b):
  if(a>b):
    print("Ist number is greater")
  else:
    print("Second num is greater or equal")

a = 9
b = 8

def isLesser(a,b):
  pass
isGreater(a,b)
calculateGmean(a,b)

