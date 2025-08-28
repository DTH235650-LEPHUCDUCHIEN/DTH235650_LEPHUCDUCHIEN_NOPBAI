import sys

# Kiểm tra số lượng tham số
if len(sys.argv) < 2:
    print("Vui lòng nhập chuỗi cần in thông qua dòng lệnh.")
else:
    # Lấy tất cả các tham số sau tên file và nối lại thành chuỗi
    chuoi = ' '.join(sys.argv[1:])
    print("Chuỗi đã nhập:", chuoi)
