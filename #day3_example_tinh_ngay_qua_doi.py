#chao, in tieu de chuong trinh
print("Hello em")
print("Chuong trinh dem ngay song con lai cua ban")
#Dat dieu kien lap
Stop = False
while Stop == False:
#Nhap du lieu
    tuoi_hien_tai = int(input("Tuoi hien tai cua ban (nam): "))
    tuoi_ket_thuc = int(input("Tuoi ket thuc cua ban (nam): "))

#tinh toan
    tuoi = tuoi_ket_thuc - tuoi_hien_tai
    ngay_con_lai = tuoi *365
#In ket qua
    print(f"So ngay con lai cua ban la: {ngay_con_lai}")

#Thay doi dieu kien lap
    option = input("Ban co muon tiep tuc hay khong?(Ok/No): ")
    if option == "N":
        Stop = True
        