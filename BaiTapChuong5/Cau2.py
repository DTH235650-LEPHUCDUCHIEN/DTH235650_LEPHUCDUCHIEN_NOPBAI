def toi_uu_chuoi(s: str) -> str:
    #Loại bỏ khoảng trắng dư thừa và tách các từ
    words = s.strip().split()

    #Viết hoa chữ cái đầu, các chữ còn lại viết thường
    words = [word.capitalize() for word in words]

    #Ghép lại thành chuỗi tối ưu
    return " ".join(words)

s = input("Nhập chuỗi danh từ:")
print("Input :", repr(s))
print("Output:", toi_uu_chuoi(s))