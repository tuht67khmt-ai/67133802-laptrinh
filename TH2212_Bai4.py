a=float((input("nhap so a:")))
b=float((input("nhap so b:")))
c=float((input("nhap so c: ")))
def so_lon_nhat(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print("so lon nhat la:",so_lon_nhat(a,b,c)) 

