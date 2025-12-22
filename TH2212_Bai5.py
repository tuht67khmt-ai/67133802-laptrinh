n=int(input("nhap so tren:"))
tong_tren = 0
for i in range(1,n+1):
    tong_tren += i
print("tong tu 1 den",n,"la:",tong_tren)
m=int(input("nhap so duoi:"))
tong_duoi = 0
for i in range(2,n+2):
    tong_duoi += i
print("tong tu 2 den",m,"la:",tong_duoi)
tong_s= tong_tren / tong_duoi
print("tong s la:",tong_s)