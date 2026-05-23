n = int(input("Nhập N: "))
a = []

for i in range(n):
    x = int(input())
    a.append(x)

print("Các phần tử chia hết cho đồng thời 2 và 3 là:")
for x in a:
    if x % 2 == 0 and x % 3 == 0:
        print(x)