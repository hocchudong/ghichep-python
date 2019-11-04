## 1. Khái niệm

Đối tượng (Object) trong thực tế là một cái gì đó hữu hình mà ta có thể thấy và cảm nhận được.

Đối tượng trong phát triển phần mềm thì không khác nhiều lắm. Chúng thì vô hình nhưng có thể làm được những việc nhất định với chúng.
Một đối tượng là một tập hợp dữ liệu và các hành vi liên quan.

Hướng đối tượng, đơn giản nghĩa là "chức năng hướng tới các đối tượng được mô hình hóa".
Nó là một trong nhiều kỹ thuật được sử dụng để mô hình hóa các hệ thống phức tạp bằng cách mô tả tập hợp các đối tượng tương tác thông qua dữ liệu và hành vi của chúng.

Trong nhiều tài liệu có nhắc đến các thuật ngữ liên quan như phân tích, thiết kế, lập trình hướng đối tượng. Đó là các giai đoạn trong phát triển phần mềm, gọi chung là hướng đối tượng.

<b>Phân tích hướng đối tượng (OOA) </b> là quá trình xem xét bài toán đặt ra để biến nó thành ứng dụng và xác định các đối tượng cũng như sự tương tác lẫn nhau của chúng.
Đầu ra của quá trình phân tích là một tập các yêu cầu.

<b>Thiết kế hướng đối tượng (OOD) </b> là quá trình chuyển đổi các yêu cầu thành đặc tả thực hiện.
Người thiết kế phải đặt tên cho các đối tượng, xác định các hành vi, xác định được đối tượng này liên quan tới đối tượng khác như nào.

<b> Lập trình hướng đối tượng (OOP) </b> là quá trình chuyển đổi các đặc tả của bước thiết kế thành chương trình theo chính xác những yêu cầu ban đầu.

## 2. Tính chất

<b> Đóng gói (Encapsulation): </b> đóng gói dữ liệu và mã chương trình thành các class để dễ quản lý. Tính chất này không cho phép người sử dụng thay đổi trạng thái nội tại của đối tượng. Chỉ có các phương thức nội tại của đối tượng mới có thể thay đối nó.
Việc cho phép bên ngoài tương tác với dữ liệu của đối tượng tùy thuộc vào lập trình, nó đảm bảo sự toàn vẹn và bảo mật của đối tượng.

<b> Trừu tượng (Abstraction): </b> Khi thiết kế các đối tượng, ta cần tìm ra những đặc trưng của chúng rồi trừu tượng hóa thành các interface và xét xem chúng tương tác với nhau như nào.

> “An abstraction denotes the essential characteristics of an object that distinguish it from all other kinds of object and thus provide crisply defined conceptual boundaries, relative to the perspective of the viewer.” — G. Booch

<b> Kế thừa (Inheritance): </b> Cho phép đối tượng có thể có những đặc tính mà đối tượng khác đã có thông qua kế thừa.
Điều này cho phép các đối tượng chia sẻ hay mở rộng các đặc tính sẵn có mà không phải định nghĩa lại.


<b> Đa hình (Polymorphism): </b> Đa hình có nghĩa là một tên, nhiều hình thức.
Đa hình biểu hiện bằng cách có nhiều phương thức với cùng một tên, nhưng cách thực hiện khác nhau.
Đa hình chia làm 2 loại : Overridding và Overloading
- **Overloading**, còn gọi là đa hình thời gian biên dich (compile-time polymorphism): trình biên dịch sẽ xác định phương thức nào sẽ được thực hiện, và quyết định này được thực hiện khi mã được biên dịch.
- **Overridding**, còn gọi là đa hình thời gian chạy (run-time polymorphism): phương thức ghi đè nào được sử dụng sẽ tùy thuộc vào kiểu của đối tượng


## 3. Vai trò

**Tính mạnh mẽ:** phần mềm có khả năng xử lý biệt lệ mà không được xác định rõ ràng.

Ví dụ :

- Phần mềm điều khiển nhà máy hạt nhân
- Phần mềm điều khiển máy bay


**Khả năng thích nghi:** phần mềm có thể phát triển theo thời gian để đáp ứng theo nhu cầu sử dụng.

=> Dễ mở rộng dự án, dễ dàng quản lý code

Ví dụ :

- Trình duyệt và các công cụ tìm kiếm được được sử dụng từ nhiều năm nay


**Khả năng tái sử dụng:** một đoạn mã có thể được sử dụng trong các hệ thống khác nhau, các ứng dụng khác nhau.

=> Tiết kiệm tài nguyên, tiền bạc và thời gian


## 4. Ví dụ minh họa (Python)

#### Tạo class

```
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
```


`empCount` là một biến thuộc class, nó có thể truy cập bằng cách `Employee.empCount`

`__init__()` là một phương thức đặc biệt - phương thức khởi tạo. Nó được gọi mỗi khi một thực thể mới của class này được tạo ra.

Các phương thức còn lại là các hàm bình thường.

#### Tạo Instance Objects

Tạo một thực thể bằng cách gọi tên class với đối số truyền vào là giá trị theo bởi hàm `__init__()`

```
# This would create first object of Employee class
emp1 = Employee("Zara", 2000)

# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
```

#### Truy cập các thuộc tính

Truy cập tới thuộc tính của `object` bằng dấu chấm `.` sau `object`
```
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```

Kết quả :

```
Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2
```

#### Thêm, sửa, xóa thuộc tính

```
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.
```

#### Lớp kế thừa

Lớp con có thể kế thừa các thuộc tính của lớp cha, và có thể sử dụng được
các thuộc tính như thể được định nghĩa trong lớp con.

```
#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
```

Kết quả:

```
Calling child constructor
Calling child method
Calling parent method
Parent attribute : 200
```


#### Ghi đè

Một lớp con cũng có thể ghi đè các phương thức của lớp cha. Lý do để ghi
đè lên phương thức lớp cha là vì bạn muốn một chức năng riêng biệt cho
phân lớp con của bạn

```
#!/usr/bin/python

class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.myMethod()         # child calls overridden method
```

Kết quả:

```
Calling child method
```

#### Nạp chồng toán tử

Một ví dụ cho việc cộng vector 2 chiều. Định nghĩa phương thức `__add__`
trong class để thực hiện cộng vector, khi đó toán tử `+` sẽ hoạt động như
mong đợi.

```
#!/usr/bin/python

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
```

Kết quả:

```
Vector(7,8)
```

#### Ẩn dữ liệu

Một thuộc tính của đối tượng thì có thể hoặc không thể hiển thị bên ngoài định nghĩa lớp.
Để thuộc tính không thể trực tiếp nhìn thấy từ bên ngoài, tên thuộc tính cần sử dụng dấu `__` ở đầu.

```
#!/usr/bin/python

class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.__secretCount
```

Kết quả:

```
1
2
Traceback (most recent call last):
   File "test.py", line 12, in <module>
      print counter.__secretCount
AttributeError: JustCounter instance has no attribute '__secretCount'
```

`__secretCount` đã bị ẩn đi bằng cách thêm `__` ở đầu tên

Bạn có thể truy cập các thuộc tính như vậy bằng cách `object._className__attrName`

Thay thế dòng cuối của đoạn code trên thành

```
...
print counter._JustCounter__secretCount
```

Kết quả:

```
1
2
2
```
