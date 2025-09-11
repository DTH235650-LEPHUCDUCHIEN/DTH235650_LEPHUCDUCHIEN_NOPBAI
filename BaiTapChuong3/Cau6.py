<<<<<<< HEAD
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
=======
print("Mình về mình có nhớ ta?\nMười lăm năm ấy thiết tha mặn nồng.\nMình về mình có nhớ không?\nNhìn cây nhớ núi, nhìn sông nhớ nguồn.")
>>>>>>> c0de2ac0eb83faaf12050d954f3f6ef691c199bb
