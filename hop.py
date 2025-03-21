# -*- coding: utf-8 -*-
"""hop.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HGe4y_SIpWWqMhI_koWTPVpus1vRv8tq

prime using function
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

"""fibonacci using function"""

def fibonacci(n):
  sequence =[]
  a , b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence
terms = int(input("Enter the terms: "))
c= fibonacci(terms)
print(c)

"""math module"""

import math
angle = float(input("Enter the angle in degrees: "))
radian = math.radians(angle)
print("sine of the angle:",math.sin(radian))
print("cosine of the angle:",math.cos(radian))