<<<<<<< HEAD
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
=======
width = 4   # chiều ngang
height = 4  # chiều dọc

for i in range(height):
    for j in range(width):
        # nếu là dòng đầu, dòng cuối, hoặc cột đầu, cột cuối -> in '*'
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
>>>>>>> c0de2ac0eb83faaf12050d954f3f6ef691c199bb
