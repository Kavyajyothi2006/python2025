# -*- coding: utf-8 -*-
"""loops.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12mn-CNbR_QqVPpd3-H6O1CN2srxuzIUD

simple calculator using if else
"""

n1=float(input("enter first number:"))
n2=float(input("enter second number:"))
operation=(input("enter operation(+,-,*,/):"))
if operation=="+":
  print(n1+n2)
elif operation=="-":
  print(n1-n2)
elif operation=="*":
  print(n1*n2)
elif operation=="/":
  print(n1/n2)
else:
  print("invalid operation")

"""leap year or not"""

year=int(input("enter year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
  print("leap year")
else:
  print("not a leap year")

"""largest of 3 numbers"""

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>=n2 and n1>=n3:
  print(n1,"is largest")
elif n2>=n3:
  print(n2,"is largest")
else:
  print(n3,"is largest")

"""check if number is -ve,+ve or 0"""

n=int(input("enter number:"))
if(n>=0):
  print(n,"is positive")
else:
  print(n,"is negative")

"""sum of all even numbers"""

a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=0
for i in range(a,b+1):
  if i%2==0:
    sum=sum+i
print("sum of even numbers is",sum)