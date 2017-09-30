#Chuong trinh doi tien tu VND sang USD va nguoc lai.
#biet 1 USD = 20.000 VND

print "Xin chao !!!"
print "Vui long nhap vao so tuong ung de quy doi"
print "Nhap 1 de doi tu USD sang VND"
print "Nhap 0 de doi tu VND sang USD"

a = input("Xin moi nhap : ")

if a == 1:
    b = input("Nhap vao so tien USD ban muon quy doi : ")
    c = b*20000.0
    print "So tien VND cua ban la : ", c
elif a == 0:
    d = input("Nhap vao so tien VND ban muon quy doi : ")
    e = d/20000.0
    print "So tien USD cua ban la : ", e
else:
    print "Nhap Sai : "