# Bài tập trong cuốn "Python for Everybody: Exploring Data Using Python3"

## Chương 1

## Chương 2: Biến, biểu thức và câu lệnh.

**Bài 1:** Gõ các dòng dưới trong chương trình biên dịch đi kèm (khi cài python) và quan sát kết quả.

 ```sh
 6 
 x = 5
 x + 1
 ```

- Tham khảo về trình biên dịch trong Python (IDLE): 
	- (1) http://prntscr.com/cxwq0g 
	- (2) http://prntscr.com/cxwpg9
	
- Chú ý: có 2 cách thao tác với python: 
	- Trình soạn thảo (editor: Sublime, notepad++, Pycham ...) 
	- Trình biên dịch (interpreter - IDLE, có sẵn khi cài đặt Python)

**Bài 2:** Viết chương trình sử dụng hàm `input()` (đối với python2.x là hàm `raw_input()` ) cho phép người dùng nhập tên và hiển thị kèm theo lời chào mừng ra màn hình. 

	Nhap ten cua ban: Cong TO
	Xin chao: Cong TO

**Bài 3:** Viết chương trình cho phép nhập số giờ lao động và giá của một giờ để tính tổng tiền phải trả. 

 ```sh
 Nhap so gio: 35
 Gia tien cua 1 gio: 2.75
 Thanh tien: 96.25
 ```

**Bài 4:** Giả sử gán các biến với các giá trị như bên dưới

 ```sh
 with = 17
 height = 12.0
 ```

Với mỗi biểu thức dưới đây, hãy điền giá trị và kiểu của chúng 

 ```sh
 1. width / 2
 2. with / 2.0
 3. height / 3
 4. 1 + 2 + 5
 ```

Sử dụng trình biên dịch của python (IDLE) để kiểm tra lại câu hỏi của bạn.

**Bài 5:** Viết chương trình thực hiện việc chuyển đổi nhiệt độ từ `C` (Celsius) sang `F` (Fahrenheit), hiển thị kết quả của việc chuyển đổi này.

## Chương 3: Điều kiện thực hiện

**Bài 1:** Viết chương trình thanh toán lương cho phép nhập vào số giờ làm và giá của 1 giờ làm việc. Nếu làm việc trên 40 tiếng thì giá tiền đối với số giờ vượt sẽ gấp 1.5 lần. Hiển thị số tiền phải trả ra màn hình.

 ```sh
 Nhap so gio: 45
 Gia cua 1 gio: 10
 Tong so tien là: 475.0
 ```
- Chú ý:
 - Số giờ vượt là 45 - 40 = 5

**Bài 2:** Hãy nâng cao chương trình ở bài tập 2, viết chương trình sử dụng `try` và `except` để xử lý tình huống nếu  các giá trị nhập vào `bài 2` không hợp lệ. Hiển thị thông báo ra mà hình. Ví dụ:

 ```sh
 Nhap so gio: 45
 Gia cua 1 gio: muoi
 Co loi xay ra, ban phai nhap vao gia tri kieu so
 ```

**Bài 3:** Viết chương trình cho phép nhập số  điểm nằm trong 0.0 tới 1.0. Nếu điểm nằm ngoài dải này hãy hiển thị ra thông báo lỗi. Nếu số điểm nằm trong dải này thì hiển thị ra xếp loại tương ứng theo bảng dưới:

```sh
Diem		Xep hang
>=0.9 		A
>=0.8 		B
>=0.7 		C
>=0.6 		D
<0.6			F
```

Ví dụ:

 ```sh
 Nhap so diem: 0.96
 A

 Nhap so diem: muoi diem
 Nhap sai gia tri

 Nhap so diem: 0.75
 C

 Nhap so diem: 10.0
 Nhap sai gia tri

 Nhap so diem: 0.5
 F
 ```

 Hãy thực thi chương trình nhiều lần như ví dụ trên để kiểm tra tính đúng đắn của chương trình.