import math
Xa = int(input("Nhập tọa độ Xa:"))
Xb = int(input("Nhập tọa độ Xb:"))
Ya = int(input("Nhập tọa độ Ya:"))
Yb = int(input("Nhập tọa độ Yb:"))
AB = math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)
Kqua = abs(AB)
print("Chiều dài của đoạn AB là:",Kqua)