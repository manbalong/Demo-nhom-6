#Bước 1. Chào
#Bước 1.1. in lời chào ra màn hình
print("Hello")
ho_va_ten= input("Hãy nhập tên của bạn: ")
#BƯớc 1.2. in tiêu đề của chương trình
print("Chương trình tính vàng của bạn")
#BƯớc 2. Nhập liệu
#BƯớc 2.1 Tuổi hiện tại
tuoi_hien_tai = int(input("Hãy nhập số tuổi hiện tại của bạn: "))
#Bước 2.2 Tuổi mong muốn
tuoi_cook = int(input("Hãy nhập tuổi bạn chết: "))
#Bước 3. Tính toán
#Bước 3.1 Tính số năm còn lại
nam_con_lai = tuoi_cook - tuoi_hien_tai
#BƯớc 3.2 Tính số tháng còn lại
thang_con_lai = nam_con_lai *12
#BƯớc 3.3 TÍnh số ngày còn lại
ngay_con_lai = nam_con_lai * 365
#BƯớc 4. In kết quả
#Bước 4.1 In số ngày
#print(f"số ngày còn lại của bạn là: {ngay_con_lai}")
print(f"Thời gian còn lại của {ho_va_ten} là bao nhiêu?")
if nam_con_lai < 10:
    print("Xin chia buồn bạn chỉ còn lại ",ngay_con_lai,"ngày để sống!!!")
else:
    print("Xin chúc mừng bạn còn lại những",ngay_con_lai,"ngày để tận hưởng cuộc sống này!!!")
#Bước 4.2 In số tháng
if nam_con_lai > 10:
    print(f"Và số tháng còn lại của bạn tận là {thang_con_lai}","tháng mờ!!!")
else:
    print(f"Tôi tiếp tục chia buồn cùng bạn nhé!!! Bạn chỉ còn lại {thang_con_lai} tháng để sống thôi")
#Bước 4.3 In số năm
if nam_con_lai > 10:
    print(f"Cuối cùng, số năm còn lại của bạn là: {nam_con_lai} năm, hú hú try yourbest to make yourlife more beatifull before you'll die")
else:
    print(f"Bạn đừng nản lòng nhé!!!! Tuy bạn chỉ còn {nam_con_lai} năm để sống, nhưng mà hãy cố gắng sống tốt phần đời còn lại của bạn sao cho thật ý nghĩa nhất nhé!!!")
