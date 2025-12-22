
import math


a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
p= a+b+c
print("chu vi tam giac la: ", p)
s= math.sqrt(p * (p - a) * (p - b) * (p - c))
print("dien tich tam giac la: ", s)