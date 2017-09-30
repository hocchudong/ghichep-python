#chuong trinh giai phuong trinh bac 2 basic.

print "Giai phuong trinh Ax2 + Bx + C = 0 tu dong"
print "Moi ban nhap day du cac thong so A, B va C"
print "Chung ta bat dau : "

import math

a = float(input("Nhap vao A : "))
b = float(input("Nhap vao B : "))
c = float(input("Nhap vao C : "))
delta = b**2 - 4*a*c

if a == 0:
    x = -c/b
    print "Nghiem cua phuong trinh la : ",x
elif delta < 0:
    print "Phuong trinh vo nghiem."
elif delta == 0:
    x1 = -b/(2*a)
    print "Phuong trinh co nghiem kep la : ", x1
else:
    x2 = (-b + math.sqrt(delta))/2
    x3 = (-b - math.sqrt(delta))/2
    print "Phuong trinh co 2 nghiem phan biet la : ", x2, x3