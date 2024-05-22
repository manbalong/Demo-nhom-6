#chao,in tieu de chuong trinh
print("Hello")
print("Chuong trinh máy tính")
#Dinh nghia ham
def ham_cong(so_dau,so_sau):
    return so_dau + so_sau
def ham_chia(so_dau,so_sau):
    return so_dau / so_sau
def ham_tru(so_dau,so_sau):
    return so_dau - so_sau
def ham_nhan(so_dau,so_sau):
    return so_dau * so_sau

stop = False

while stop == False :
    so_1 = int(input("Hay nhap so dau tien: "))
    so_2 = int(input("hay nhap so sau: "))
    phep_tinh = input("Hay nhap phep tinh ( + , - , * , / ) : ")
    if phep_tinh == "+":
        so_can_tinh = ham_cong(so_1,so_2)
        print(so_can_tinh)
    elif phep_tinh == "-":
        so_can_tinh = ham_tru(so_1,so_2)
        print(so_can_tinh)
    elif phep_tinh == "*":
        so_can_tinh = ham_nhan(so_1,so_2)
        print(so_can_tinh)
    elif phep_tinh == "/":
        so_can_tinh = ham_chia(so_1,so_2)
        print(so_can_tinh)
    else:
        print("Phep tinh khong ton tai")

    thu_lai = input("Ban co muon thu nhap lai phep tinh khong (Co / Khong)? : ")
    if thu_lai == "Khong":
        stop =  True

