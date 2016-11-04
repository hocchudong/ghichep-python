#!/bin/python
#------------------------------------------------------
# - Viet chuong trinh chuyen doi tu do C sang do F. Nguoi
#	dung nhap vao do C, chuong trinh hien thi do F
# - Cong thuc: F = C * (9 / 5) + 32
# - Su dung ham input() de nhap do C vao
# - Su dung ep kieu de hien thi dung
#------------------------------------------------------
# Bat dau
do_C = input('Nhap gia tri (do C):  ')
do_F = do_C * 9.0 / 5.0 + 32		# Su dung cong thu de chuyen do C sang do F
# Hoac
# do_F = do_C * float(9) / float(5) + 32
print ""
print "Nhiet do la: ", do_F , "F"
