#Lý thuyết tổng hợp từ chapter 1.

```sh
Tại sao chúng ta cần phải viết một chương trình ?
```

- Viết ra một chương trình là một hoạt động rất sáng tạo và bổ ích , chúng ta có thể viết một chương trình với rất nhiều 
lý do khác nhau nhưng thông thường chúng ta viết chương trình dùng để giải quyết các vấn đề công việc. Cuốn sách này 
sec cho chúng ta cách làm thế nào để viết một chương trình và sẽ giúp chúng ta viết chương trình để giải quyết các vấn đề 
bằng chính kỹ năng của bản thân.

```sh
Tại sao phải cần tìm hiểu để viết ra một chương trình.
```

-  Thông thường khi các lập trình viên làm việc họ sẽ làm việc trực tiếp với máy tính , và máy tính cũng có ngôn ngữ riêng của nó
vậy làm thế nào mà một lập trình viên có thể nói chuyện được với máy tính? Để có thể giao tiếp với máy tính thì chúng ta có thể dùng 
ngôn ngữ máy, tuy nhiên ngôn ngữ máy tương đối khó để chúng ta có thể sử dụng thành thực do đó chúng ta cần có một ngôn ngữ bậc cao hơn
giúp cho quá trình làm quen được dễ dàng hơn một trong các ngôn ngữ bậc cao đó là Python.

```sh
Tổng quan về kiến trúc phần cứng máy tính.
```

- Trước khi bắt đầu vào học một ngôn ngữ chúng ta cần tìm cách chỉ dẫn để máy tính phát triển phần mềm . Chúng ta cần phải 
biết một chút về làm thế nào mà một chiếc máy tính được xây dựng lên . Nếu như bạn đã từng tháo máy tính hay chiếc điện thoại 
ra thì chắc hẳn bạn sẽ thấy được các phần như sau :

![scr1](http://i.imgur.com/VZvHELO.png)

- Các định nghĩa : 
 <ul>
  <li>Cental Process Unit (CPU) : Là bộ não của máy tính tại đó mọi thông tin, thao tác, dữ liệu sẽ được tính tóan
  kỹ lưỡng và đưa ra lệnh điểu khiển mọi hoạt động của máy tính. </li>
  <li>Main Memory : Được sử dụng để lưu trữ các dữ liệu mà CPU cần ghấp (nhanh) , Main Memory nhanh gần như CPu nhưng 
  các dữ liệu thường bị mất đi khi chúng ta tắt máy.</li>
  <li>Secondary Memory : Cũng được sử dụng để lưu trữ thông tin nhưng nó nhiều cũng như chậm hơn Main Memory. Ưu điểm của 
  bộ nhớ phụ là nó có thể lưu trữ dữ liệu ngay cả khi không có điện vào máy tính . (CD, USB,...) </li>
  <li>Input and Output Devices : Đơn giản là màn hình, bàn phím, chuột, loa ,....</li>
  <li>Ngày nay hầu hết các máy tính đều kết nối mạng để lấy dữ liệu qua mạng , chúng ta có thể nghĩ rằng mạng là công cụ lấy dữ 
  liệu khá chậm, vì vậy trong một nghĩa nào đó mạng chậm hơn và đôi khi không đáng tin cậy bằng bộ nhớ thứ cấp.</li>
 </ul>

```sh
Python - reserved words:
```

![2](http://i.imgur.com/MdEtMw0.png)

- Đây là những từ khóa , những từ `riêng biệt` trong python, nó đã được định nghĩa sẵn do đó chúng ta không được phép 
sử dụng nó để đặt tên cho biến,...

```sh
Chương trình đầu tiên "Hello world" : 
```

- Trong tất cả các ngôn ngữ lập trình nếu như chúng ta tìm hiểu và học, thì chương trình quen thuộc "Hello world" luôn 
là chương trình đầu tiên để bắt đầu học một ngôn ngữ.
- Để in ra màn hình dòng chữ "Hello world" Python sử dụng `Print "[Nội dung]"` :

```sh
>>>Print "Hello world"
```

```sh
Python là trình thông dịch ?
```

- Trong lập trình thì chúng ta có 2 loại là thông dịch và biên dịch , Python là ngôn ngữ theo kiểu thông dịch . 
- Thế thông dịch là gì ? Biên dịch là gì? 

| Title | Biên dịch | Thông dịch |
|-------|-----------|------------|
| Định Nghĩa | - Chương trình được viết được biên dịch ra thành ngôn ngữ máy trên một HDH xác định trước và chỉ chạy trên HDH đó (C++ -> .exe chỉ chạy trên Win, C++ -> .o chạy trên Unix/Linux …..) | - Trong thông dịch thì mã nguồn không được dịch trước thành ngôn ngữ máy mà mỗi lần cần chạy chương trình thì mã nguồn mới được dịch để thực thi từng dòng 1 (line by line). Tất cả các ngôn ngữ không biện dịch ra mã máy điều phải sử dụng trình thông dịch (PHP, WScripts, Perl, Linux Shell, Python….). Các ngôn ngữ theo trình thông dịch thường được gọi là script (kịch bản) |
|| - Ưu điểm của trình biên dịch là chương trình được tối ưu tốt cho HĐH và kiến trúc phần cứng ngay lúc dịch sang mã máy. | - Trình thông dịch thì có ưu điểm là có thể chạy trên nhiều HĐH và kiến trúc máy tính khác nhau, miễn là có bộ thông dịch tương ứng trên HDH. |
|| - Tuy quá trình này tốn thời gian, nhưng chỉ thực hiện có 1 lần mà thôi. | - Trình thông dịch thì mỗi lần chạy sẽ chuyển chương trình sang mã máy, mỗi lần dịch thì thời gian tốt ít thôi, nhưng bù lại có thể lần nào chạy cũng phải dịch (trừ khi bộ thông dịch cache lại kết quả của lần dịch trước đó). |
|| - Trình biên dịch tạo ra file executable lúc này đã là mã máy, nên trên đĩa nó bao nhiêu thì load lên memory nó sẽ xấp xỉ bấy nhiêu. | - Trình thông dịch thì trên memory còn có bộ thông dịch, và bộ thông dịch phải load chương trình nguồn lên rồi dịch thành mã máy…cho nên thường quá trình chạy 1 chương trình thông dịch sẽ tốn memory hơn. |

