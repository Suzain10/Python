# -*- coding: utf-8 -*-
"""Exercise_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10zXYnwPyxKdwDabPN5jCEvUtjy69fD_1
"""

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("The sum of a and b is",a+b)
print("The subtraction of a and b is",a-b)
print("The multiplication of a and b is",a*b)
print("The division of a and b is",a/b)
print("The exponential of a and b is",a**b)

while True:
  print("Select operation: ")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice=(int(input("Enter your choice (1/2/3/4/5): ")))

  if choice not in [1,2,3,4,5]:
    print("Invalid input")

  if choice == 5:
    print("Exiting..")
    break

  num1= float(input("Enter the first number: "))
  num2= float(input("Enter the second number: "))

  if choice == 1:
    print("Result", num1+num2)
  elif choice == 2:
    print("Result", num1-num2)
  elif choice == 3:
    print("Result", num1*num2)
  elif choice == 4:
    if num2 == 0:
      print("Cannot divide by 0")
    else:
      print("Result", num1/num2)
  break