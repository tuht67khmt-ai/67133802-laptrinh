n = int(input("Nhập N: "))
a = []
tong = 0

for i in range(n):
    x = int(input())
    a.append(x)

for x in a:
    if x % 2 == 0 or x % 3 == 0:
        tong += x

print("Tổng các phần tử chia hết cho 2 hoặc 3 là:", tong)
