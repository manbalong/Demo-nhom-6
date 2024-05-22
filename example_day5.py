#in ten chuong trinh, loi
print(f"xin chao cac ban!\nChuong trinh nay se den so lan xuat hien mot ky tu trong doan van cua ban.\nHy vong co ich cho ban")
#Nhap lieu; nhap chuoi, nhap ky tu den trong chuoi
    #nhap tao bien chuoi
stop =False
while stop ==False:
    bien_string = input("Hay nhap doan van cua ban:\n")
        #nhap tao bien ky tu
    bien_ky_tu = input("Hay nhap ky tu ban muon den trong doan van: ")
    #Dem
        #Tao bien dem
    bien_dem = 0
    #tao vong lap for de dem
    for item in bien_string:
        if item ==bien_ky_tu:
            bien_dem +=1

    #in ket qua theo dinh format string
    print(f"Ket qua den cua chuong trinh nhu sau:\n\t So lan xuat hien ky tu \'{bien_string} trong doan van: \'{bien_string}\' la: {bien_dem} lan ")

    #tao dieu kien rang co muon nhap lai khong?
    thu_lai = input("Ban co muon nhap lai doan van khong? (Co/Khong): ")
    if thu_lai == "Khong":
        stop = True
