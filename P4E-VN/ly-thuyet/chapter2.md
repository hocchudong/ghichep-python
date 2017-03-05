#Lỹ thuyết tổng hợp từ chapter 2. Biến - Biểu Thức - Các Câu Lệnh.

```sh
Giá trị và loại giá trị.
```

- Giá trị là một điểu cơ bản khi làm việc một chương trình giống như một lá thư hay một vài con số. Các giá trị ví dụ 
như là : 1, 2 và "Hello world" . Những giá trị này thuộc các thể loại khác nhau :
 <ul>
  <li>1,2 : Thuộc kiểu số nguyên.</li>
  <li>Hello world : là một chuỗi.</li>
 </ul>

```sh
Biến (variables)
```

- Một trong những tính năng mạnh mẽ nhất của một ngôn ngữ lập trình đó là khả năng thao tác biến . Một biến là một cái 
tên dùng để chỉ một giá trị.

- Ví dụ về một biến .

```sh
>>>a = 6
>>>print "day la so : ", a
```

- Làm thế nào để có thể khai báo một biến ?
 <ul>
  <li>Tên biến bắt đầu bằng [A-Z] hoặc [a-z] hoặc dấu _ (gạch dưới) và các ký tự tiếp theo có thể là [a-z], [A-Z], [0-9] hoặc dấu _</li>
  <li>Tên biến trong Python không chứa các ký tự đặc biệt %, @, $, ^, &...</li>
  <li>Phân biệt in hoa và in thường, tên biến không chứa khoảng trống (space).</li>
  <li>Tên biến không được trùng với các từ keywords như bảng bên dưới.</li>
 </ul>

![3](http://i.imgur.com/FmJRYXi.png)

- Không cần khai báo kiểu dữ liệu của biến như C/C++, Pascal...
- Có cơ chế cấp địa chỉ và ép kiểu tự động – gán dữ liệu kiểu gì thì nhận kiểu đó.
- Gán giá trị cho biến dùng dấu = (bằng)
- Ví dụ : x = 1, y = 2, bien = 3

![4](http://i.imgur.com/L8hI1Au.png)

```sh
Nhập xuất dữ liệu.
```

- Nhâp dữ liệu trực tiếp khi lập trình :

- Ví dụ : Viết một file `gioithieu.py` có đầy đủ thông tin họ tên, trường, lớp, tuổi , quê quán và in ra màn hình :

```sh
print "ho va ten : Pham Thanh Dat"
print "Truong : Mat Ma"
print "lop : AT11C"
print "Tuoi : 20"
print "Que Quan : Ninh Binh"
```

- Nhập dữ liệu từ bàn phím .

- Có 2 kiểu đó là :

```sh
raw_input("thông báo !!!") - Dữ liệu nhập vào kiểu String
``

Và 

```sh
input("Thông báo !!!") - Dữ liệu nhập vào kiểu số.
```

- Ví dụ : Viết chương trình nhập thông tin sinh viên từ bàn phím :

```sh
a = raw_input("Ho va Ten : ")
b = input("Tuoi : ")
c = raw_input("Lop : ")
d = raw_input("Que Quan : ")

print a
print b
print c
print d

```

- Đối với bản Python 3.0 trở đi thì thông tin nhâp vào từ bàn phím chỉ còn dùng input("") cho cả dữ liệu nhập vào là 
String cũng như dữ liệu nhập vào là số. raw_input("") bị bỏ đi.

```sh
Các toán tử.
```
- Toán tử số học : 

| Toán tử | Miêu tả |
|---------|---------|
| // | Thực hiện phép chia, trong đó kết quả là thương số sau khi đã xóa các chữ số sau dấu phảy |
| + | Phép cộng |
| - | Phép trừ |
| * | Phép nhân |
| / | Phép chia lấy nguyên |
| % | Phép chia lấy phần dư |
| ** | Lũy thừa |

- Ví dụ :

```sh
>>>a = 3
>>>b = 4
c = a + b
print "ket qua phep cong : ", c
d = c*a
print "ket qua phep nhan : ", d
```

- Toán tử quan hệ :

| Toán tử | Miêu tả |
|---------|---------|
| < | Nhỏ hơn |
| > | Lớn hơn |
| <= | Nhỏ hơn hoặc bằng |
| >= | Lớn hơn hoặc bằng | 
| == | Bằng |
| != | Không bằng |

ví dụ : Viết chương trình giải phương trình bậc 2 :

```sh
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
```

- Một số toán tử khác :

![1-desktop](http://i.imgur.com/0wUdxXH.png)