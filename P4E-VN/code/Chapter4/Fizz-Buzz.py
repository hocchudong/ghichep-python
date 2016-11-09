# Write your code below!
#Viet mot chuong trinh in tu 1 den 100.
#Doi voi boi 3 thi in "Fizz"
#Doi voi boi 5 thi in "Buzz"
#Doi voi ca boi 3 va 5 thi in "FizzBuzz"
#In ra so lan xuat hien cua "Fizz" va so lan xuat hien cua "Buzz" vaf "FizzBuzz"
list = []
for i in range(1,101):
    if(i%3 == 0):
        print "Fizz"
        list.append('Fizz')
        #gh.write(',')
    elif(i%5 == 0):
        print "Buzz"
        list.append('Buzz')
        #gh.write('"Buzz"')
        #gh.write(',')
    elif(i%3 == 0 and i%5 == 0):
        print "FizzBuzz"
        list.append('FizzBuzz')
        #gh.write('"FizzBuzz"')
    else:
        print "%d" %i
print list.count('Fizz')
print list.count('Buzz')
print list.count('FizzBuzz')
