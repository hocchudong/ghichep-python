#Viet mot chuong trinh phong van down gian
#ghi lai thong tin vao 1 file
#o day la file phongvan.txt
print "Xin chao !!! "
print "Cong ty abc dang co nhu cau tuyen dung vi tri xyz"
print "Moi ban nhap cac thong tin de gui den nha tuyen dung : "
a = raw_input("Ho va ten : ")
b = raw_input("Tuoi : ")
c = raw_input("Que Quan : ")
d = raw_input("Noi o hien nay : ")
e = raw_input("SDT lien he : ")
f = raw_input("Email : ")
g = raw_input("Co bao nam kinh nghiem o vi tri xyz : ")
h = raw_input("Ban co the chap nhan muc luong bao nhieu 1 thang : ")

k = open('phongvan.txt','a')
k.write(a)
k.write('\n')
k.write(b)
k.write('\n')
k.write(c)
k.write('\n')
k.write(d)
k.write('\n')
k.write(e)
k.write('\n')
k.write(f)
k.write('\n')
k.write(g)
k.write('\n')
k.write(h)
k.write('\n')
k.close()
