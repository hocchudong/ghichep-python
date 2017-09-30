#!/usr/bin/python
# -*- coding: utf8 -*-
#Ép kiểu.
# Có 3 kiểu dữ liệu chính trong Python là int , float và String. 
#Giả sử chúng ta nhập vào một giá trị có kiểu float , tuy nhiên chúng ta muốn nó hiện ra kiểu int chúng ta có thể làm như sau :
a = int(3.5)
print a 

# Lưu ý rằng int chỉ lấy phần nguyên trước dấu phẩy chứ không có chức năng làm tròn như kiểu 3,9 sẽ thành 4.
# Thông thường kết quả nhập vào từ bàn phím của chúng ta sẽ được chọn kiểu int để ép thành float đối với một số biến cần float , chúng ta làm như sau :

b = float(input("Nhap vao gia tri : "))
print b # giả sử ta nhập vào 5 , kết quả in ra màn hình sẽ là 5.0
