a = float(input("Nhập vào giá trị a = "))
b = float(input("Nhập vào giá trị b = "))
operation = input("Nhập phép tính (+,-,*,/): ")

if operation == "+":
    result = a + b
    print("Kết quả: ",result)
elif operation == "-":
    result = a - b
    print("Kết quả: ",result)
elif operation == "*":
    result = a * b
    print("Kết quả: ",result)
elif operation == "/":
    if b != 0:
        result = a / b
        print("Kết quả: ",result)
    else:
        print("Lỗi: Không thể chia hết cho 0.")
else:
    print("Phép toán không hợp lệ.")