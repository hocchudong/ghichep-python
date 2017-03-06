## Cách định dạng text trong python 3

- Tham khảo: https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3

## Giới thiệu

- Chuỗi được được tạo ra bởi các chữ cái và ký tự. 
- Python có khả năng định dạng và thao tác với các chuỗi.

## String Literals

- Có hai khái niệm cần phân biệt: `string literal` và `string value`.
- `String literal`: Là chuỗi mà chúng ta nhìn thấy trong mã nguồn của python
- `String value`: Là chuỗi được hiển thị ra trong lệnh ping
- Ví dụ: Gõ dòng sau trong IDLE hoặc python CLI
	```sh
	print ("Hoc Chu Dong \n 2017")
	```

- Kết quả là, ta sẽ nhìn thấy ký tự `\n` trong đoạn code nhưng ko thấy trong lúc hiển thị, thay vào đó là xuống dòng.
	```sh
	Hoc Chu Dong
	 2017
	```

## Dấu nháy kép và dấu nháy đơn

- Chuỗi có thể bao bọc trong dấu nháy đơn hoặc dấu nháy kép.
- Nếu trong chuỗi có chứa các dấu nháy đơn thì bao đóng chuỗi là dấu nháy kép và ngược lại
	```sh
	my_str = 'Hoc Chu Dong"s'
	print my_str
	```

- Hoặc
	```sh
	my_str = 'Hoc Chu Dong"s'
	print my_str
	```

### Chuỗi trên nhiều dòng

- Để in chuỗi trên nhiều dòng ta sử dụng cặp ba dấu nháy đơn `'''` hoặc ba dấu nháy kép `"""`, ví dụ:
	```sh
	print '''Hoc Chu Dong
	2017
	'''
	```

- hoặc 
	```sh
	print """Hoc Chu Dong
	2017"""
	```

- Kết quả của các đoạn lệnh trên là
	```sh
	Hoc Chu Dong
	2017
	```



