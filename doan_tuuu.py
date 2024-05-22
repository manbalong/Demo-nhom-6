print("Chào mừng bạn đến với trò chơi đoán từ")
stop = False
while stop == False:
    dap_an = "vịt"  # Đáp án của trò chơi
    goi_y = ["Đoán 1 từ và là con vật có màu trắng",
             "Gợi ý thứ hai: Có 2 chân",
             "Gợi ý cuối cùng: Biết bơi và đẻ trứng"]

    for hint in goi_y:
        print(hint)
        doan = input("Hãy nhập dự đoán của bạn: ")

        if doan == dap_an:
            print(f"Chính xác! Chúc mừng bạn đã dành chiến thắng trò chơi này! Với đáp án là: {dap_an}")
            break  # Thoát khỏi vòng lặp nếu đoán đúng

        print("Sai rồi! Hãy thử lại")

    else:
        print(f"Xin chia buồn bạn đã thất bại trong trò chơi này! Chúc bạn may mắn lần sau! Đáp án đúng là: {dap_an}")

    option = input("Bạn có muốn thử lại trò chơi không (Y/N): ")
    if option == 'N':
        stop = True