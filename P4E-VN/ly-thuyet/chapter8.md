#Tổng hợp lý thuyết chapter 8 .

#List.

```sh
Tạo một list mới.
```

 -Một số cách thường dùng để tạo một list mới như sau :

 >>>a = [2,3,4,5]
 >>>b = ['messi','neymar','ronaldo']

- Nếu như chúng ta muốn tạo một list trống , chúng ta làm như sau :

>>>c = []

```sh
Có thể thay đổi các thông số có sẵn trong 1 list.
```

- Cũng giống như String, List cũng có thể thay đổi :

- Ví dụ như sau :

>>>a = ['Pham','Thanh','Dat']
>>>a[1] = Van
>>>print a

Kết quả : Pham Van Dat

```sh
List Operations.
```

>>>a = [1,2,3]
>>>b = [4,5,6]
>>>c = a + b
print c

Kết qủa sẽ là : [1,2,3,4,5,6]

- Tương tự với phép cộng ta có phép nhân như sau :

>>>a = [3]
>>>b = a * 4
print b

Kết quả là : [3,3,3,3]

```sh
List Slices.
```
- Tương tự với chuỗi .

- Ví dụ ta có một list như sau :

a = [1,2,3,4,5,6]

>>>a[0:2]
[1,2,3]
>>>a[:4]
[1,2,3,4,5]
>>>a[4:]
[2,3,4,5,6]

```sh
List method.
```

- http://ksec.info/threads/bai-9-1-cau-truc-du-lieu-trong-python.61/

```sh
Sự tương tác giữa List là String
```

>>>string = 'dat'
>>>a = list(string)
>>>print a

Kết quả là : ['d','a','t']