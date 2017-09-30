#!/usr/bin/python
# -*- coding: utf8 -*-
def giatri_lonnhat():
    largest = None
    print 'Before:', largest
    for itervar in [3, 41, 12, 9, 74, 15]:
        if largest is None or itervar > largest :
            largest = itervar
        print 'Giá trị lớn nhất :', largest
    print 'Lớn hơn tất cả là :', largest

def giatri_nhonhat():
    smallest = None
    print 'Before:', smallest
    for itervar in [3, 41, 12, 9, 74, 15]:
        if smallest is None or itervar < smallest:
            smallest = itervar
    print 'Giá trị nhỏ nhất hiện tại là :', itervar, smallest
    print 'Vậy giá trị nhỏ nhất là :', smallest 

giatri_lonnhat()
giatri_nhonhat()
