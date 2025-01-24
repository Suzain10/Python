# -*- coding: utf-8 -*-
"""Python_Basics_Rev.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ojLUKqblcYsDR5QUjfdJtO1dDZOWr7K

**Module** is like a code library which can be used to borrow the code written by somebody else, is of 2 types:
**Built-in** **modules** are included in Python's standard library and do not require installation and can be used using import. Example: math, os etc.
**External modules** are not included in the standard library and need to be installed using a package manager like pip. Example: numpy, pandas etc.
"""

print("Hi I am \"Suzain\".")  #Escape Sequence

print("My name is \"Suzain\",\nI live in \"India\",\nI love \"Animals\".")

new_var = print("My name is \"Suzain\" " ," I live in \"India\"", sep="and")
new_var

print("Suzain", "24","Female", sep = "\n")  #Separator

'''new_var = print("My name is \"Suzain\" " ," I live in \"India\"", sep="and")
new_var'''                   ##Multi-line Comment
print("Hello")

"""**Typecasting**: Conversion of one data type to another.
Has 2 types:  
**Implicit Typecasting:** Here, Python automatically converts one data type to another to avoid data loss or errors during operations.

**Explicit Typecasting:** It is when you manually convert one data type to another using functions like int(), float(), str(), etc.


"""

a = 1
b = 2
print(type(a))

a = "1"
b = "2"
print(type(a))
print(a + b)

a = int(2.2)
b = 2.2
print(type(a))

#Implicit Typecasting:
a = 2  #integer
b = 2.2  #float
print(a + b)  #float

#Explicit Typecasting:
a = "1"  #string
a = int(a)
print(type(a))

"""**Taking input from User using input() function:**"""

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("The sum of a and b is:",a+b)

name = input("Enter your name: ")
print("Hello ", name  + "! :)")

"""**Strings**: A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or ''' ''').

*Immutable:* Once a string is created, its content cannot be changed.


*Ordered:* Strings maintain the order of characters, so indexing and slicing are possible.
"""

print("\"The Sun is awake so I am awake!\"\n", "\"Do you wanna build a Snowman?\"")

frozen = """Do you wanna build a snowman

Or ride our bikes around the halls?

I think some company is overdue, I've started talking to

The pictures on the walls

Hang in there, Joan

It gets a little lonely, all these empty rooms

Just watching the hours tick by

(tick, tock, tick, tock, tick, tock, tick, tock)

Elsa?

Please, I know you're in there

People are asking where you've been

\"They say have courage and I'm trying to

I'm right out here for you

Just let me in

We only have each other, it's just you and me\"

What are we gonna do?

\"Do you wanna build a snowman?\""""
print(frozen)

nm = """Harry"""
print(nm[-4:-2])
print(len(nm))

name = input("Enter your name: ")
count = (len(name))
print("Your name has \"",count,"\" characters.")

char_count = name[0:5]
print(char_count)

char_count = name[:9]
print(char_count)

char_count = name[:] #By default takes values from 0 to len of string
print(char_count)

for i in name:
  print(name)

for i in name:
  print(i)

"""**String Methods:**
The strip() method in Python does not limit its operation to only the exact characters at the ends of the string.
Instead, it works by removing all occurrences of any character specified in its argument from the start and end of the string.
It does not remove characters from the middle of the string.

The **rstrip() method** in Python is used to remove any trailing characters (characters at the end of a string).
By default, it removes whitespace (spaces, tabs, newlines) from the right side of the string
but you can also specify a set of characters to remove.
"""

str = name.rstrip("!")
print(str)

str = name.rstrip("")
print(str)

str_1 = "TheJuTngleTBook@#$%**)(||\:;)"
print(str_1)

result = str_1.rstrip("Thko@#$%*)(|\\:;")
print(result)

str = "TheJungleBook@#$%**)(||\:;)"
str_1= str.rstrip("@#$%**)(||\:;)")
print(str_1)

str_2 = str_1.upper()
print(str_2)

str_2 = str_1.lower()
print(str_2)

