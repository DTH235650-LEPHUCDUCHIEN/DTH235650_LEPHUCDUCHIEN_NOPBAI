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
<<<<<<< HEAD
    print("Phép toán không hợp lệ.")
=======
    print("Phép toán không hợp lệ.")
>>>>>>> 4d7ada004f0e82736f2e4b2f17169d3257014926
