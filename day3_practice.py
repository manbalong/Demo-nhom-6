#Doan tu: choi doan 1 tu co san trong may theo cac goi y
#Chuong trinh dua ra mot so goi y cho phep nguoi cung doan tu (sau mot so lan goi y)
#Neu doan dung chuong trinh se bao win, neu sai chuong trinh bao fail
#Hoi nguoi dung co choi lai hay thoat ra
import getpass
stop = False
while stop == False:
    tu_can_doan = "Doraemon"
    so_lan_goi_y = 3  # Số lần gợi ý cho phép
    goi_y = 0

    print("Chào mừng bạn đến với trò chơi đoán từ!")
    print("Tôi đã chọn một từ từ danh sách. Bạn có 3 lần gợi ý để đoán từ đó.")

    while goi_y < so_lan_goi_y:
        dua_ra_goi_y = input("Viet goi y cho nguoi choi: ")
        doan_cua_ban = input("Dap an cua ban: ")
        if doan_cua_ban == tu_can_doan:
            print(f"Chính xác! Bạn đã đoán đúng từ là:{tu_can_doan}")
            print("Bạn đã chiến thắng!")
            break
        else:
            print("Sai rồi! Hãy thử lại.")
            goi_y += 1
    if goi_y > 2:
        print("Bạn đã hết số lần gợi ý.")
        print(f"Từ cần đoán là: {tu_can_doan}")
        print("Bạn đã thua!")

    #tao dieu kien co muon thu lai khong?

    cau_lenh = input("Ban co muon choi lai hay khong? (Có/Không): ")
    if cau_lenh == "Không":
        stop = True
