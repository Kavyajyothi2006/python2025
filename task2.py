# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Khr_mDiiTaUflIPvmrfD9nwWH_oasMyq

multiplication generator
"""

n=int(input("enter a number:"))
print(f"the product of{n}:")
for i in range(1,11):
    print(n,"x",i,"=",n*i)

"""grading system"""

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks <= 89:
        return "B"
    elif marks <= 74:
        return "C"
    else:
        return "F"

marks = int(input("Enter your marks: "))
grade = calculate_grade(marks)
print("Your grade is:", grade)

"""sum of first n natural numbers"""

def sum_natural(n):
    return (n * (n + 1)) // 2

n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is:", sum_natural(n))

"""prime number"""

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))


if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")

"""number reversal"""

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

num = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(num))
