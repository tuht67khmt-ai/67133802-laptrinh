n=int(input("nhap n:"))
a,b =0,1
tong=0 
Fibonacci = []
for i in range(n):
    Fibonacci.append(a)
    a, b = b, a + b
print("Cac so Fibonacci dau tien:",Fibonacci)
tong = sum(Fibonacci) 
print("Tong cac so Fibonacci dau tien la:",tong)

