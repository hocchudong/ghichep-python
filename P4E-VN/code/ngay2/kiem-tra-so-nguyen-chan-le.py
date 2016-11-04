#Viet chuong trinh kiem tra xem so do co phai so nguyen duong hay khong, neu dung kiem tra xem la so chan hay le.

a = input("Nhap vao so ban muon : ")
if (a > 0):
    print a, "la so nguyen duong"
    if (a%2 == 0):
        print a, "La so chan"
    else:
        print a, "La so le"
elif (a < 0):
    print a, "la so nguyen am"
else:
    print a, "La so 0"