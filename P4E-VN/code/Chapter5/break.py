#!/usr/bin/python
# -*- coding: utf8 -*-
#Chương trình test thử câu lệnh break. 

n = 0

while n < 10:
    print "Đây là số : ", n
    n = n + 1
    if n ==7:
        break
print "Done!!!"

#Nếu như gặp số 7 chương trình sẽ tự thoát cho dù 7,8,9 là những số đều nhỏ hơn 10, nhưng nó không xét đến nữa.