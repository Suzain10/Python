# -*- coding: utf-8 -*-
"""While loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Mqk0PHwerDln15NYS7jqwksBrOz0YKD
"""

#While loop:Executes till the condition is true.
i = 0
while(i<=3):
 print(i)
 i=i+1

i = int(input("Enter the number: "))
while(i<=30):
 i = int(input("Enter the number: "))
 print(i)
print("Done with the loop")

#Decrementing while loop:
count = 5
while(count>0):
  print(count)
  count=count-1

#Else with while loop:
count = 5
while(count>0):
  print(count)
  count=count-1
else:
  print("I am inside else!")

#Do while loop:Not in Python
'''do{
  #loop body; #Executes atleast once even if condition is false
}while(condition);'''