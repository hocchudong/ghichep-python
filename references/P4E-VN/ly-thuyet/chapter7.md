#Lý thuyết tổng hợp chapter 7.

#Files.

```sh
Mở file.
```

- Để mở một file chúng ra thực hiên cú pháp như sau ?

```sh
>>>f = open('name.txt','a')
```

- Trong đó :
 <ul>
  <li>f là tên biến chúng ta đặt.</li>
  <li>open là thao tác mà chúng ta thực hiện với file. Có các thao tác như : open (mở ), write (viết), close (đóng).</li>
  <li>name.txt : Là tên file mà chúng ta cần thao tác.</li>
  <li>a là tùy chọn mở tập tin và thêm vào cuối file . CHúng ta có một số tùy chọn cơ bản như  r : chỉ đọc , w : chỉ ghi , a mở và ghi xuống cuối file.</li>
 </ul>

- Để viết file trước tiên chúng ta cần mở file trước , các cú pháp lần lượt như sau :

```sh
>>>f = open('phongvan.txt','a')
>>>f.write("Toi la Pham Thanh Dat. Toi vua thay doi file phongvan.txt")
>>>f.close()
```

- Ngoài tùy chọn a, chúng ta có thể tùy chọn w như sau :

```sh
>>>f = open('phongvan.txt','w')
>>>f.write("Toi la Pham Thanh Dat. Toi vua thay doi file phongvan.txt")
>>>f.close()
```

- Để đọc file, hay hiển thị file lên màn hình chúng ta thực hiện như sau :

```sh
>>>f = open('phongvan.txt','r')
>>>f.read()
>>>f.close()
```

- Một lưu ý nhỏ khi chúng ta ghi file trước khi đọc file thì vị trí con trỏ lúc đó đang ở cuối file lên sẽ không đọc 
được, chúng ta cần phải chỉnh lại con trỏ trước khi đọc.

```sh
>>>f = open('phongvan.txt','a')
>>>f.write('Them dong nay')
>>>f.seek(0)
>>>f.read()
>>>f.close()
```

- Sử dụng vòng lặp tương tác với file.


- Sử dụng vòng lặp để đếm số dòng trong file

f = open('fraction.txt','r')
dem = 0
for line in f:
    dem = dem + 1
print "so dong la : ", dem


- Tìm kiếm thông qua file.


- Giả sử có 1file phongvan.txt chúng ta cần tìm ra những ứng viên ở Hà Nội , chúng ra sẽ làm như sau :

fhand = open('phongvan.txt','r')
for line in fhand:
    if line.startswith('Hà Nội') :
        print line

`Chúng ta có thể sử dụng kết hợp với continue và break để cho cách giải quyết các bài toán trở lên linh động hơn`

