#Lý thuyết tổng hợp chapter 6.

#Strings.

- Ví dụ về chuỗi :

```sh
>>>hoaqua = "Chanh"
>>>teb = "Pham Thanh Dat"
```

- Lấy kí tự theo vị trí :

```sh
>>>a = "hanoi"
>>>b = a[0]
>>>print b
```

=> Kết quả nhận được sẽ là 'h'.

- Trong python số thứ tự về vị trí được đánh từ 0 , nên khi chúng ra chỉ định ký tự số 0 thì đó là ký tự đầu tiên 'h'

- Để lấy về độ dài của chuỗi chúng ra sử dụng hàm len()

- Ví dụ như sau :

```
>>>a = "hanoi"
>>>print len(a)
```

=> Kết quả chúng ta thu được sẽ là : 5.

```sh
String Slice
```

- Một đoạn của String được gọi là `Slice`

ví dụ :

```
>>>a = "Pham Thanh Dat"
>>>print a[0:5]
Pham
>>>print a[6:12]
Thanh
```

- Chúng ta cũng có thể lấy từ kí tự đầu đến giới hạn nào đó hoặc từ kí tự nào đó đến kí tự cuối như sau :

```sh
>>>print a [:5]
Pham
>>>print a[6:]
Thanh Dat
```


- Thay thế một kí tự trong chuỗi 

```sh
>>>a = "Alo Dat"
>>>new_a = 'B' + a[1:]
Blo Dat
```

- Sử dụng với vòng lặp và count.


a = "Pham Thanh Dat"
dem = 0
for i in a:
    if i == 'a':
        dem = dem + 1
    print "Số chữ a hiện có là ", dem
print "Có tất cả số chữ a là : ", dem


- Các phương thức với String.


- https://docs.python.org/2/library/stdtypes.html#
string-methods.