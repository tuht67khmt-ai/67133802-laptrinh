import math
n = int(input("Nhập n: "))
S = 0
for i in range(n):
    S = math.sqrt(3 + S)
print("S4(n) =", S)