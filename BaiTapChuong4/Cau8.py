import math
x = float(input("Nhập x (x>0):"))
a = float(input("Nhập a (a>0, a!=1):"))
if x>0 and a>0 and a!=1:
    logax=math.log(x)/math.log(a)
    print(f"log{a}({x}) = {logax}")
else:
    print("Giá trị không hợp lệ! Yêu cầu: x > 0, a > 0 và a ≠ 1")