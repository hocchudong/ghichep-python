#Lý thuyết tổng hợp chapter 3.

#Conditional execution.

- Ví dụ về thực thi điều kiện :

```sh
>>> 5 == 5
True
>>> 5 == 6
False
```

- Để thực thi được các điều kiện chúng ta cần sử dụng đến các vòng lặp và các toán tử đã nhắc đến trong chapter trước .

- Các vòng lặp thường sử dụng như `if-else` , `while` , `for`

- Ví dụ về `if-else` :

```sh
>>> x = 3
>>> if x < 10:
...
print 'Small'
...
Small
>>>
```

- Ví dụ về `while` : 

```sh
a = 2
while a < 10:
    print a
    a = a + 1
print "Thanks for wacth !!!"
```

- Ví dụ về `for` : 

```sh
sott = [1, 2, 3, 4]
monhoc = ['Tieng Anh', 'Toan', 'Ly', 'Hoa']
for a in sott
    print "tiet %d la mon %s" % sott % monhoc
```