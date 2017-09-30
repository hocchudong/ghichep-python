#!/usr/bin/python
# -*- coding: utf8 -*-
#test thu function voi def.
#su dung bang cach print_thongtin()
def print_thongtin():
    print "Toi la Pham Thanh Dat"
    print "Tuoi 20"
    print "Hoc tai KMA"
#print_thongtin()

#su dung bang cach repeat_thongtin()
def repeat_thongtin():
    print_thongtin()
    print_thongtin()
#repeat_thongtin()

#biến trong hàm

def dat(x):
    if x == 'kma':  
        print "La Pham Thanh Dat"
        print "Lop AT11C"
    elif x == 'uit':
        print "La ong Dat nao day"
        print "Lop nao day"
    elif x == 'hust':
        print "Them mot ong Dat khac"
        print "Ở một lớp nào đó khác ở Hust"
    else:
        print "Sao toàn người tên Đạt thế này"
dat('kma')
dat('uit')
dat('hust')
dat('vovan')