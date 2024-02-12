# -*- coding: utf-8 -*-
"""For Loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hVEBL0bSdZmCK02-S8eWIcOiIzvBnJEp
"""

#Loops:To execute a group of statements a certain number of times we use loops.
#Majorly two types of loops:For and while
#For loop:
name = 'Abhisheb'
for i in name:

  print(i,end=",")
  if(i=="b"):
    print("\nThis is something special")
  else:
    print("  Wrong")

#List:
colors = ["Red","Orange","Blue","Green","Purple","Pink"]
for color in colors:
  print(color)
  for i in color:
    print (i)

#printing using range function:
for k in range(10): #Automatically starts from 0 to 10
  print(k)
for k in range(1,20):  #Can specify the start and end of range
  print(k)

#Exploring third parameter of range(x,y,z):
for k in range(1,20,3):  #Can specify the start and end of range and the sequence you want to follow
  print(k)