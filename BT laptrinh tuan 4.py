import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setup(2.IO.OUT)
IO.setup(3.IO.OUT)
IO.setup(4.IO.OUT)
IO.setup(5.IO.OUT)
IO.setup(6.IO.OUT)
IO.setup(7.IO.OUT)
IO.setup(8.IO.OUT)

import RPi.GPIO as GPIO
import time

# Thiết lập chế độ chân GPIO
GPIO.setmode(GPIO.BOARD)

# Danh sách chân GPIO cho các LED
led_pins = [11, 12, 13, 15, 16, 18, 22, 7, 3, 5]

# Khởi tạo các chân GPIO là OUTPUT
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Hàm để hiển thị số lên LED
def display_number(number):
    binary_number = bin(number)[2:].zfill(10)  # Chuyển số sang dạng nhị phân 10-bit
    for i, pin in enumerate(led_pins):
        GPIO.output(pin, int(binary_number[i]))  # Đặt trạng thái của LED tương ứng

# Chạy các số từ 0 đến 9
try:
    while True:
        for i in range(10):
            display_number(i)
            time.sleep(1)  # Đợi 1 giây giữa mỗi số
finally:
    GPIO.cleanup()  # Dọn dẹp các chân GPIO khi kết thúc chương trình

