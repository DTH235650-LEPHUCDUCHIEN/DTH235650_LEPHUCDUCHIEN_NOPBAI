def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    # Trường hợp số nhỏ hơn 10
    if n < 10:
        return don_vi[n]

    # Trường hợp từ 10 đến 19
    if n < 20:
        if n == 10:
            return "mười"
        else:
            return "mười " + don_vi[n % 10]

    # Trường hợp số có phần chục và đơn vị
    if n < 100:
        if n % 10 == 0:
            return chuc[n // 10]
        else:
            return chuc[n // 10] + " " + don_vi[n % 10]


# Nhập số từ người dùng
n = int(input("Nhập một số (tối đa 2 chữ số): "))

# In ra cách đọc số
print(doc_so(n))