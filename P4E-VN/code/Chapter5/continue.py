#!/usr/bin/python
# -*- coding: utf8 -*-
#test thử với continue. 

#for letter in 'Python':  
#   if letter == 'h': 
#        continue 

#    print 'Current Letter :', letter

n = 0
while n < 10:
    if n == 7:
        continue
    print "Đây là số : ", n
    n = n + 1
print "Done!!!"