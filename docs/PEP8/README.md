
### PEP-8 (Python Enhancement Proposal 8) - Style Guide for Python Code

Tác giả Python, ông Guido Van Rossum có câu :

> The code is read much more often than it is written.

Đó là lý do chúng ta cần phải tổ chức code sao cho dễ đọc.
PEP-8 như là một chuẩn được quy định bởi ông và đồng nghiệp.
Nó trình bày một số điểm giúp cho code của bạn có tổ chức và dễ đọc.

Bài viết sẽ nêu một vài điểm chính:

- Giới thiệu
- Thụt đầu dòng
- Chiều dài dòng tối đa
- Dòng trống
- Khoảng trắng trong biểu thức và câu lệnh
- Mã hóa file nguồn
- Liên quan tới `import`
- Comment
- Module level dunders (ví dụ: `__all__`, `__author__`)
- Đặt tên
- Công cụ kiểm tra


#### Giới thiệu

Python trong những năm gần đây đang trở thành một trong những ngôn ngữ rất được ưa chuộng.
Với nhiều module mở rộng, nó trở nên phổ biến trong lĩnh vực data science và web development

Bạn có thể tận dụng tốt hơn các ưu điểm của Python nếu biết thể hiện nó tốt trong đoạn mã của bạn.

Về vấn đề này, có một số nguyên tắc mà ta có thể thấy được khi chạy

```
import this
```

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Trên đây là những nguyên tắc mà lập trình viên Python cần áp dụng.

"Readability counts." là mối quan tâm hàng đầu khi viết code.
Tính dễ đọc giúp cho các lập trình viên khác hay các nhà khoa học có thể hiểu và đóng góp cho code của bạn.

Các phần tiếp theo sẽ cung cấp chi tiết hơn về một số quy tắc hay sử dụng nhất để viết code theo PEP-8.

#### Thụt đầu dòng

Khi lập trình Python, thụt lề là điều chắc chắn cần phải quan tâm. Với mỗi đoạn code cùng mức phải thụt lề bằng nhau.
Khuyến nghị là 4 khoảng trắng cho mỗi mức.

Ví dụ:

```
if True:
    print("If works")
```

Bên cạnh đó có một vấn đề tranh luận khá nhiều là sử dụng `tab` hay `spaces`, xem thêm [link](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-useink-tabs/)

Nhìn chung, `spaces` được ưa thích hơn, nhưng nếu bạn làm việc với những script đã sử dụng `tab` thì nên theo với `tab` để cho thống nhất.

Lưu ý là Python3 không cho phép trộn 2 loại thụt lề này, bạn chỉ được sử dụng một trong hai.

#### Chiều dài dòng tối đa

Số ký tự tối đa cho một dòng code là 79 ký tự.

Điều này giúp hầu hết màn hình không phải cuộn thanh ngang để đọc hiểu code.

Với các dòng comment thì nên là 72 ký tự

Với các dòng code dài thì nên cắt thành các dòng ngắn bằng cách đưa các biểu thức vào các cặp ngoặc đơn, cắt dòng khi hoàn thành biểu thức
và thêm "\\" rồi xuống dòng tiếp theo viết tiếp.

Với code có các biểu thức, toán tử, toán hạng dài thì ngắt trước toán hạng.

*Ví dụ:*

```
# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

#### Dòng trống

Trong Python, các top-level function và class cách nhau 2 dòng trống.
Các method định nghĩa trong class cách nhau 1 dòng trống.


#### Khoảng trắng trong biểu thức và câu lệnh

Sử dụng theo các ví dụ sau :

- Bên trong dấu ngoặc đơn, ngoặc vuông, ngoặc nhọn:
```
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
```

- Giữa dấu phẩy và ngoặc đơn:
```
Yes: foo = (0,)
No:  bar = (0, )
```
- Trước dấu phẩy, chấm phẩy, hai chấm:
```
Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x
```
- Tuy nhiên, dấu hai chấm khi có vai trò là toán tử thì số khoảng trắng 2 bên bằng nhau:
```
Yes:

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
No:

ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```
- Trước mở ngoặc để bắt đầu đối số của một hàm:
```
Yes: spam(1)
No:  spam (1)
```
- Trước mở ngoặc vuông để bắt đầu index
```
Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]
```
- Sử dụng một khoảng trắng cho gán biến
```
Yes:

x = 1
y = 2
long_variable = 3
No:

x             = 1
y             = 2
long_variable = 3
```

#### Mã hóa file nguồn

Máy tính không thể lưu trữ con số, ký tự, hình ảnh dưới dạng nguyên bản mà nó phải chuyển sang giá trị 0 1.
Để chuyển sang giá trị nhị phân, nó cần sử dụng một quy tắc để mã hóa. Một số bộ mã hóa tiêu biểu có thể nhắc đến như ASCII, UTF-8, ...


ASCII là định dạng phổ biến nhất cho các file văn bản trên máy tính và Internet. Mỗi ký tự được mã hóa bằng 7 bits.

Unicode là hệ thống sử dụng cho trao đổi, xử lý, hiển thị các văn bản viết bằng các ngôn ngữ đa dạng.
Unicode được thiết kế để cung cấp tất cả các hệ thống chữ viết trên thế giới.
Nó sử dụng 3 bộ mã hóa khác nhau: UTF-32, UTF-16, UTF-8.

Khai báo mã hóa :

```
# -*- coding: utf-8 -*-
```

Trong Python3, mặc định sử dụng mã hóa UTF-8 còn với Python2 là ASCII.

Nhưng nếu bạn dùng Python2 mà có một chuỗi non-ASCII như "Flügel"

```
>>> s="Flügel"
>>> s
'Fl\xc3\xbcgel'
>>> print(s)
Flügel
```

Ký tự `ü` đã được chuyển thành `\xc3\xbc` bằng cách dùng `.encode()` và `.decode()`

```
>>> u = u"Flügel"
>>> u
u'Fl\xfcgel'
>>> u.encode('latin_1')
'Fl\xfcgel'
````

```
>>> s = "Flügel"
>>> s.encode('latin_1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 2: ordinal not in range(128)
>>> s
'Fl\xc3\xbcgel'
```

Chuỗi u được mã hóa Unicode, sử dụng bảng mã latin_1 cho kết quả như giá trị chuỗi s, trong khi s không thể mã hóa được.

```
>>> s.decode('latin-1')
u'Fl\xc3\xbcgel'
```

Chuỗi s được giải mã cho kết quả như chuỗi u.

#### Liên quan tới `import`

Mỗi module được import trên một dòng

```
Yes: import os
     import sys

No:  import sys, os
```

Hoặc có thể viết :

```
from subprocess import Popen, PIPE
```

import thường đặt đầu file, ngay sau docstring và trước các module toàn cục và hằng số.

Thứ tự các nhóm import:

- Các thư viện chuẩn
- Các thư viện third-party
- Các thư viện local

Nên đặt một dòng trống với các nhóm import

Import tuyệt đối và tương đối :

- Import tuyệt đối là sử dụng đường dẫn tuyệt đối của các function, class, ngăn cách bởi dấu `.`.
- Import tương đối là sử dụng đường dẫn tương đối với vị trí hiện tại của file Python
- Import tuyệt đối được ưa thích hơn vì dễ đọc, nhưng nếu ứng dụng phức tạp, bạn vẫn có thể dùng import tương đối
- [PEP-328](https://docs.python.org/2.5/whatsnew/pep-328.html) mô tả chi tiết về vấn đề này

Import từ một class từ module
```
from mymodule import MyClass
from foo.bar.yourmodule import YourClass
```
hoặc
```
import mymodule
import foo.bar.yourmodule
```
và sau đó sử dụng "mymodule.MyClass", "foo.bar.yourmodule.YourClass".

Tránh sử dụng wilcard khi import, vì nó không làm tăng tính dễ đọc. Ví dụ :

```
from scikit import *
```

#### Comment

Sử dụng block comment để giải thích cho một đoạn code phức tạp, và được thụt lề cùng mức với mã.
Mỗi dòng comment bắt đầu với `#` và một khoảng trắng. Nếu comment nhiều hơn một đoạn, các đoạn nên phân cách bằng một dòng chứa một dấu `#`

Sử dụng inline comment ngắn gọn và có ý nghĩa. Nó nên được cách ra ít nhất 2 khoảng trắng so với câu lệnh, tiếp đó là dấu `#` và một khoảng trắng.

Viết docstrings sử dụng cặp dấu """ cho tất cả các module, function, class, method public. Các method non-public thì không cần docstrings nhưng cũng nên có dòng comment để mô tả nó làm gì. Comment này nên đặt sau dòng `def`. Chi tiết về docstrings xem thêm tại [PEP-257](https://www.python.org/dev/peps/pep-0257/)

#### Module level dunders

Module level "dunders" là những module với 2 dấu gạch dưới ở đầu và cuối. Ví dụ : `__all__`, `__author__`, `__version__`.
Nó nên được đặt sau docstrings của module và trước import, ngoại trừ import `__future__`.

Ví dụ:

```
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

#### Đặt tên

Phân biệt hoa thường

Sử dụng phong cách under_score

Tên biến dùng chữ thường, tên hằng dùng chữ hoa

Tên 1 ký tự nên tránh I, L, O vì chúng nhìn dễ lẫn với một vài font

Tên package viết thường, ngắn gọn, không nên dùng _

Tên module, function viết thường, ngắn gọn và được dùng "_" để phân biệt trong trường hợp tên có hai từ.

Tên class viết theo kiểu CapWords

#### Kiểu import

Không nên import tớ tận Class, mà chỉ import đến package.

*Ví dụ:* Khi có một class Bar nằm trong package tên foo.py, thì khi muốn sử dụng class Bar thì ta nên import như sau:

```
import foo

name = foo.Bar()

```

Nên chỉ rõ đường dẫn khi import, không nên dùng kiểu `import *` hoặc `import .`


#### Công cụ kiểm tra

Để kiểm tra xem code của bạn có tuân theo đúng PEP-8 không, có một vài công cụ kiểm tra:

- [pycodestyle](https://github.com/PyCQA/pycodestyle) tên trước đây là `pep8`
- [coala](https://github.com/coala/coala)
- [pep8online](http://pep8online.com/)

Trên một vài IDE như Pycharm cũng có tích hợp sẵn kiểm tra PEP-8.

#### Ref

https://www.python.org/dev/peps/pep-0008/

https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code
