#khai niem chung ham
#su dung de to chuc chuong trinh theo phuong cach lap trinh huong thu tuc
#Ham de thục hien mot vai hành động: print
#Ham de tinh toan dua ra mot gia tri, nhieu gia tri, du lieu
#Su dung ham trong chuong trinh

#Python la ngon ngu thong dich
#Buoc1. Định nghĩa hàm

#Bước 2, Gọi hàm

#Truyền giá trị và tham số trong hàm
def tinh_tong(a, b):
    tong = a + b
    return tong

# Gọi hàm và in kết quả
print(tinh_tong(3,5))# Output: 8

def ten_cua_ban():
    ten = "man ba long la toi"
    return ten
print(ten_cua_ban())

def whoareyou():
    ten_ban_la ='Long dep trai'
    return ten_ban_la
def ban_o_dau():
    toi = "Toi o Bac ninh province va ten toi là "
    ten_noi_sinh_song = toi + whoareyou()
    return ten_noi_sinh_song

print(ban_o_dau())

def ham_nhan(a, b):
    return a * b

def ham_tinh_tong_voi_nhan(a, b, c):
    tich = ham_nhan(b, c)
    tong = a + tich
    return tong

# Gọi hàm và in kết quả
print(ham_tinh_tong_voi_nhan(2, 3, 4))  # Output: 14

#Từ khóa return trong hàm
#Từ khóa dùng cho loại hàm trả về giá trị, hoặc dữ liệu
#Từ khóa này cũng l kết thúc hàm
def ham_cong3(i=100, j=10, k=1):
    bien = i+j+k
    return bien
print(f"Tong cua 3 so i , j , k là : {ham_cong3()}")
#Phạm vi của biến trong và ngoài hàm
