## Làm việc với chuỗi trong python3
- Chuỗi là một trong các kiểu dữ liệu phổ biến sử dụng trong Python
- Tham khảo: https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3

## Giới thiệu

- `String` - Chuỗi là sự kết hợp tuần của một hoặc nhiều ký tự (chữ cái, số, ký tự)
- String là kiểu dữ liệu không thay đổi (inmutable)
- Trong tài liệu này sẽ hướng dẫn bạn tạo, in, thao tác cơ bản với chuỗi.

## Tạo và in ra chuỗi (Strings)

- Chuỗ trong python được nằm trong cặp dấu nháy đơn `''` hoặc cặp dấu nháy kép `""`
- Ví dụ
	```sh
	"Day la mot chuoi"
	```

- Hoặc 
	```sh
	'Mot chuoi trong python'
	```

- Để in ra một chuỗi trong python ta làm như sau:
	```sh
	print ("Hoc Chu Dong")
	```

- hoặc
	```sh
	my_string = "Chu Dong Hoc"
	print (my_string)
	```

Kết quả là:
	```sh
	Chu Dong Hoc
	```

## Nối tiếp chuỗi

- Để nối tiếp chuỗi trong Python3, ta sử dụng phép cộng (`+`)
- Ví dụ dưới nối các chuỗi `HOC`, `CHU`, `DONG`
	```sh
	print ("HOC" + "CHU" + "DONG")
	```

- Kết quả là
	```sh
	HOCCHUDONG
	```

- Nếu muốn có các khoảng cách giữa các chuỗi, ta làm như sau
	```sh
	print ("HOC " + "CHU " + "DONG")
	```

- Chú ý về khoảng trống giữa các chuỗi, kết quả là:
	```sh
	HOC CHU DONG
	```

- Lưu ý: Khi thực hiện nối tiếp chuỗi cần chú ý kiểu của chuỗi phải phù hợp, ví dụ dưới sẽ gây ra lỗi bởi vì 2 chuỗi có kiểu khác nhau, một là `string` và một là `integer`, ví dụ:
	```sh
	print ("HOC CHU DONG" + 2017)
	```

- Kết quả là
	```sh
	>>> print ("HOC CHU DONG" + 2017)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: must be str, not int
	```

- Nhưng nếu xử lý để đưa `2017` vào dấu nháy đơn hoặc nháy kép thì sẽ có kết quả đúng, bởi vì lúc đó `2017` sẽ là chuỗi, ví dụ:
	```sh
	print ("HOC CHU DONG " + "2017")
	```

- Kết quả là
	```sh
	HOC CHU DONG 2017
	```


