# Giới thiệu các hàm về chuỗi trong python
## Giới thiệu

- Python có một số hàm được dựng sẵn (built-in) dành cho kiểu dữ liệu là string.
- Trong bài viết này giới thiệu về một số hàm build-in đối với `string` trong python

## Tạo ra chuỗi có ký tự thường và ký tự hoa

- Hàm `str.upper()` sẽ cho kết quả trả về là chuỗi bao gồm các chữ cái viết hoa
- Hàm `str.lower()` sẽ cho kết quả trả về là chuỗi bao gồm các chữ cái viết thường
- Do `string` là kiểu dữ liệu không thay đổi được nên chuỗi sinh ra sẽ là một chuỗi mới.
- Những ký tự không phải là chữ cái sẽ không thay đổi được.

- Ví dụ dưới sẽ chuyển đổi dòng `Hoc Chu Dong 2017` thành chuỗi gồm các chữ cái viết hoa và số 2017
	```sh
	my_str = "Hoc Chu Dong 2017"
	print (my_str.upper())
	```

- Chuỗi mới sẽ là:
	```sh
	HOC CHU DONG 2017
	```

- Sử dụng hàm `lower()` với chuỗi trên thì kết quả đầu ra là chuỗi toàn ký tự viết thường, số 2017 sẽ được giữ nguyên.
	```sh
	my_str = "Hoc Chu Dong 2017"
	print (my_str.lower())
	```

- Kết quả là:
	```sh
	hoc chu dong 2017
	```

## Phương thức `Boolean` (Logic) trong `string`

- Python có phương thức làm việc với chuỗi để trả ra giá trị có kiểu `Boolean` (kiểu logic `True` - `False`)
- Phương thức này hữu ích khi sử dụng để tạo các form nhập từ người dùng. Ví dụ đối mã quốc gia thì bạn chỉ cho phép là các ký tự số, khi hỏi về tên người thì chỉ cho phép là các ký tự chữ.
- Dưới là bảng của các phương thức làm việc với chuỗi và trả về kết quả là `True` hoặc `Flase`

[string-boolean](../images/bt-string04.png)

