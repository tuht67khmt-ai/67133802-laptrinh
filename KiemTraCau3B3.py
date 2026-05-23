n = int(input("Nhập N: "))
a = []
for i in range(n):
    a.append(int(input()))
dem = 0
print("Các số Armstrong là:")
for x in a:
    s = 0
    t = x
    k = len(str(x))
    while t > 0:
        s = s + (t % 10) ** k
        t = t // 10
    if s == x:
        print(x, end=" ")
        dem = dem + 1
print("\nSố lượng số Armstrong:", dem)