#viet chuong trinh nhap vao so nguyen duong
#Sau do chuyen doi sang co so 2,8, va 16.

print "---|| Xin chao ||---"
print "Day la may chuyen co so tu dong"

a = input("Xin moi nhap vao so nguyen duong : ")

if a >= 0:
    b = bin(a)
    c = hex(a)
    d = oct(a)
    print "co so 2 la : ", b
    print "co so 16 la : ", c
    print "co so 8 la : ", d 
else:
    print "La so am."
