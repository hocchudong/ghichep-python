#Lý thuyết tổng hợp Chapter 5.
#Vòng lặp.

```sh
Upadating Variable.
```

- Giả sử ta có biểu thứ sau :

```sh
>>>x = x + 1
```
- Ta có thể hiểu như sau . Ban đầu khởi tạo một biến x sau đó cộng thêm một giá trị và cập nhật lại giá trị của biến x.
- Lưu ý rằng trước khi cập nhật lại giá trị của biến thì phải khai báo giá trị cho biến , có nghĩa là :

```sh
>>>x = 0
>>>x = x + 1
```

- Vòng lặp While.


- Xét một ví dụ như sau :

n = 1

while n < 7:
    print n
    n = n + 1
print "Chương trình thử nghiệm done !!!"

- Ở ví dụ trên chúng ta thấy được :
 <ul>
  <li>Bước đầu biến n được khai báo với giá trị là 0</li>
  <li>Dùng vòng lặp while với điều kiến n < 7</li>
  <li>Chương trình sẽ kiểm tra điều kiện xem n có nhỏ hơn 7 không, nếu nhỏ hơn sẽ in ra màn hình n</li>
  <li>Sau đó tăng n lên một đơn vị, rồi quay lại kiểm tra điều kiện, nếu đúng thì tiếp tục in ra n, nếu sai sẽ dùng chường trình lại.</li>
 </ul>

