from multiprocessing.managers import ListProxy
import string
import datetime
import time



###   05/02/2024   ###

# name = "osho raj sheelup"
# fname = 'osho'
# mname = 'raj'
# lname = 'sheelup'
# int1 = 10
# int2 = 20
# a = True if 'o' not in name else False
# a
# print("This", "is", "VS", "Code")
# print("This"+"is"+"VS"+"Code")
# print("My name is %s"%name)
# print("My name is %s %s %s"%(fname, mname, lname))
# print("My name is {} {} {}".format(fname, mname, lname))
# print("My name is {2} {1} {0}".format(fname, mname, lname))
# print("Sum of {} and {} is {}".format(1,2,1+2))
# print(f"My name is {name}")
# print(f"{int1:^50}")


# num1 = int(input("Enter a number: "))
# if num1%2==0:
#     print(f"{num1} is even")
# else:
#     print(f"{num1} is odd")

# age = int(input("Enter your age: "))

# if age<18:
#     print("Too young to vote")
# elif age<80:
#     print("You can vote")
# else:
#     print("Too old to vote")



###   12/02/2024   ###

# a = int(input("Enter a number: "))
# type(a)

# # WAP to take a number as an input from the user as an
# # input from the user and find if its even or odd

# num = int(input("Enter a number: "))
# if num%2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# for i in "Data Science":
#     print(i, end=" ")

# # WAP to take an year as in input from the user
# # and check if its a leap year

# year = int(input("Enter a year: "))
# if (year%400 == 0 or year%4) == 0 and year%100 != 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# # WAP to find the sum of digits of given number

# num = input("Enter a number: ")
# sum = 0
# for i in num:
#     sum = sum+int(i)
# else:
#     print(f"Successfully added")
# print(sum)

# num = 12345
# while num > 5:
#     print("Osho")
#     num = num//5
# else:
#     print(f"Successfully completed")

# # WAP to reverse the number
# num = list(input("Enter a number: "))
# num.reverse()
# for i in num: print(i,end="")

# # num[-1:-5:-1]

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("""Which operation to perform\n\
# 1.Addition\n\
# 2.Subtraction\n\
# 3.Multiplication\n\
# 4.Division\n\
# 5.Exponential""")

# def calc():
#     choice = int(input(">>> "))
#     match choice:
#         case 1:
#             res = num1+num2
#         case 2:
#             res = num1-num2
#         case 3:
#             res = num1*num2
#         case 4:
#             res = num1/num2
#         case 5:
#             res = num1**num2
#         case _:
#             print("Invalid input\n")
#             calc()



###   19/02/2024   ###

# #WAP to find wheater the given number is prime or not
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# elif num == 1:
#     print("1 is neither prime nor composite")
# else:
#     print(f"{num} is not a prime number")

# # WAP to print all the prime numbers in a given range
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# for i in range(start, end+1):
#     if i > 1:
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 break
#         else:
#             print(i, end=" ")

# # WAP to print all the number from 1 to 100 except 50
# for i in range(1, 101):
#     if i == 50:
#         continue
#     print(i, end=" ")



###   11/03/2024   ###

# import numpy as np
# List = (list(range(1, 11)))
# List
# List.append(11)
# List.insert(0, 0)
# List.remove(5)
# List.pop(3)
# List.clear()
# List.extend([11, 12, 13])
# List.index(11)
# List.count(11)
# List.sort()
# List.reverse()
# List.copy()
# List2 = np.array(List)
# List2.min()
# List2.max()
# List2.mean()
# List
# List2

# array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array2d.resize(9,1)
# array2d.T
# array2d

# Tuple = (1,2,3,4,5,6,7,8,9,10)
# type(Tuple)
# len(Tuple)
# min(Tuple)
# max(Tuple)
# sum(Tuple)
# Tuple.index(5)
# Tuple.count(3)
# Tuple[1:5]
# Tuple[::2]
# Tuple[::-1]
# t = sorted(Tuple)
# t
# type(t)
# Tlist = list(Tuple)
# Tlist.append(11)
# Tlist.insert(0, 0)
# Tlist.remove(5)
# Tlist.pop(3)
# Tlist.extend([11, 12, 13])
# Tlist.clear()
# Tuple = tuple(Tlist)
# Tuple
# Tlist

choice = int(input("Enter number from 1 to 5:"))
match choice:
    case 1:
        print(f"you have selected 1")
    case 2:
        print(f"you have selected 2")
    case 3:
        print(f"you have selected 3")
    case 4:
        print(f"you have selected 4")
    case 5:
        print(f"you have selected 5")
    case _:
        print("You didnt select any number from 1 to 5")

# WAP to find the factorial of a given number
num = int(input("Enter a number: ")); fact = 1
for i in range(1, num+1):   fact = fact*i
print(f"The factorial of {num} is {fact}")