#!/usr/bin/python
# -*- coding: utf8 -*-
#test max , min trong python.
#đối với max , min đứng trước trước các String , chức năng của nó sẽ chỉ ra chữ cái có vị trí lớn nhất và nhỏ nhất trong chuỗi. 
#Ví dụ với chuỗi "Hello world" chúng ta dễ dàng nhận ra rằng chữ "W" có giá trị vị trí lớn nhất trong chuỗi
big = max("Hello world")
print big #Kết quả thu được của chúng ta là w

#Cũng với ví dụ trên ta thử với min:

small = min("Hello world")
print small #Kết quả sẽ là khoảng trống bỏi vì khoảng trống được coi là giá trị nhỏ nhất.

#Chúng ta cùng thử với chuỗi "Helloworld"

small = min("Helloworld")
print small #Kết quả thu được sẽ là ký tự H.

#Chúng ta cùng thử với cả chữ và số và khoảng trống.

big = max("abc va 123")
small = min("abc va 123")
print big #thu được v
print small #thu được khoảng trống

#Từ đây chúng ta rút ra được kết luận vị trí từ nhỏ đến lớn là : khoảng trống < số < chữ

#Hàm đếm len()
#Dùng để đếm các kí tự có trong chuỗi :
#Ví dụ

print len(big) #kết quả thu được là 1
print len("hello world") #kết quả thu được là 11