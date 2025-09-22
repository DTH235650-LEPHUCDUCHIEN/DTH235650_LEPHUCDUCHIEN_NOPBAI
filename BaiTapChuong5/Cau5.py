# Chương trình đếm các loại ký tự trong chuỗi

s = input("Nhập vào một chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0

# Tập hợp nguyên âm (bao gồm cả hoa và thường)
nguyen_am = "aeiouAEIOU"

for ch in s:
    if ch.isupper():           # Chữ in hoa
        hoa += 1
    elif ch.islower():         # Chữ in thường
        thuong += 1
    elif ch.isdigit():         # Chữ số
        so += 1
    elif ch.isspace():         # Khoảng trắng
        khoangtrang += 1
    else:                      # Ký tự đặc biệt
        dacbiet += 1

    # Kiểm tra nguyên âm hay phụ âm
    if ch.isalpha():           # Nếu là chữ cái
        if ch in nguyen_am:
            nguyenam += 1
        else:
            phuam += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số chữ là ký tự đặc biệt:", dacbiet)
print("Số chữ là khoảng trắng:", khoangtrang)
print("Số chữ là Nguyên Âm:", nguyenam)
print("Số chữ là Phụ âm:", phuam)
