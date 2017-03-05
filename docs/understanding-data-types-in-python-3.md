## Tìm hiểu về các kiểu dữ liệu trong python 3

## Tham khảo:

- https://www.digitalocean.com/community/tutorials/understanding-data-types-in-python-3

## Giới thiệu

- `Python` cũng giống các ngôn ngữ khác, có kiểu của dữ liệu (Data Types).
- Kiểu dữ liệu sẽ xác định giá trị được gán.
- Trong bài này giới thiệu cơ bản về kiểu dữ liệu chính trong `python3`.

## Kiến thức nền tảng

- Kiểu dữ liệu quyết định giá trị thực sự của dữ liệu, ví dụ: số nguyên dương `(0, 1, 2, 3 ...)` hoặc số nguyên - kiểu intergers `(... -2, -1, 0, 1, 2 ...)` hoặc các số trong toán học như số PI `(PI = 3.14)`

- Chúng ta có thể kết hợp các kiểu dữ liệu với nhau, ví dụ phép cộng của các số hoặc các kiểu dữ liệu, ví dụ
	```sh
	3 + PI
	```

Kết quả là: 
	```sh
	3 + PI = 3 + 3,14 = 6.14
	```

- Có các kiểu dữ liệu phổ biến sau trong `Python3`

## Số học (Numbers)
- Tron python3 có hai kiểu số, kiểu `integer` và `float`
- `Integer` là số mà `KHÔNG` có `chấm`, ví dụ: 10, 13, 19, 300
- `Float` là số có dấu `chấm`, ví dụ: 19.0, 12.3 

### Interger

- Integer trong pythong được viết là `int`
- Lưu ý dấu `,` và `.` trong python khi viết.
- Ví dụ:
	```sh
	print (10)
	```

- Kết quả là
	```sh
	10
	```

### Floating-Point Numbers

- `Floating-Point Numbers` trong python có kiểu là `float`
- Ví dụ: 
	```sh
	print (13.7)
	```

- Kết quả là
	```sh
	13.7
	```

## Booleans (Kiểu logic)

- Kiểu logic có 2 giá trị là `True` và `False`
- Ví dụ:
	```sh
	my_bools = 5 > 9
	print (my_bools)
	```
- Kết quả:
	```sh
	False
	```

## String (Kiểu chuỗi)

- Giá trị là các chuỗi ký tự
- Lưu ý: Kiểu chuỗi được được nằm trong dấu cặp dấu nháy đơn `''` hoặc nháy kép `""`
- Ví dụ: 
	```sh
	my_string = "To Thanh Cong"
	print (my_string)
	```

- Kết quả: 
	```sh
	To Thanh Cong
	```

## List (Kiểu danh sách)

- Có giá trị là một danh sách (hay gọi là danh sách các phần tử)
- Được nằm trong cặp dấu `[` và `]`
- Kiểu list là kiểu dữ liệu có thể thay đổi được (mutable)

- Ví dụ kiểu danh sách là các số integers
	```sh
	[-3, -2, -1, 0, 1, 2, 3]
	```

- Ví dụ kiểu danh sách là các số float
	```sh
	[3.14, 9.23, 111.11, 312.12, 1.05]
	```

- Ví dụ danh sách là các chuỗi
	```sh
	['hong', 'lan', 'man', 'anh tuc']
	```

- Khi định nghĩa một list các chuỗi ta thực hiện như sau
	```sh
	my_list =  ['hong', 'lan', 'man', 'anh tuc']
	```

- Để in ra list trên thực hiện như sau:
	```sh
	print (my_list)
	```

- Kết quả là:
	```sh
	['hong', 'lan', 'man', 'anh tuc']
	```

## Tuple 

- Giá trị nằm trong cặp đấu ngoặc đơn `(` và `)`
- Giá trị của tuple là không thay đổi được (inmutable)


```sh
ĐANG CẬP NHẬT
```

## Dictionaries - Kiểu từ điển

- Là kiểu dữ liệu ánh xạ trong python (Python’s built-in mapping type)
- Được biểu diễn bởi cặp `key` và `value`


```sh
ĐANG CẬP NHẬT
```

## Bài tập



