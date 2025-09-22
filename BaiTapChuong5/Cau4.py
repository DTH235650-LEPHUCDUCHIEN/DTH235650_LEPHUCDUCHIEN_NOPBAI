# CÁC HÀM QUAN TRỌNG TRONG XỬ LÝ CHUỖI PYTHON

s = "  Hello Python 123  "

functions = [
    ["len(s)", "Độ dài chuỗi", len(s)],
    ["str(123)", "Chuyển sang chuỗi", str(123)],

    ["s.upper()", "In hoa toàn bộ", s.upper()],
    ["s.lower()", "In thường toàn bộ", s.lower()],
    ["s.capitalize()", "Viết hoa chữ cái đầu", s.capitalize()],
    ["s.title()", "Viết hoa chữ cái đầu mỗi từ", s.title()],
    ["s.swapcase()", "Đảo ngược hoa-thường", s.swapcase()],

    ["s.isalpha()", "Chỉ chứa chữ cái?", s.isalpha()],
    ["s.isdigit()", "Chỉ chứa số?", s.isdigit()],
    ["s.isalnum()", "Chữ + số?", s.isalnum()],
    ["s.isspace()", "Chỉ khoảng trắng?", s.isspace()],
    ["s.isupper()", "Toàn chữ hoa?", s.isupper()],
    ["s.islower()", "Toàn chữ thường?", s.islower()],

    ["s.find('Py')", "Vị trí đầu tiên của 'Py'", s.find("Py")],
    ["s.rfind('o')", "Vị trí cuối cùng của 'o'", s.rfind("o")],
    ["s.replace('Python','Java')", "Thay thế chuỗi", s.replace("Python","Java")],

    ["s.split()", "Tách chuỗi thành list", s.split()],
    ["' - '.join(['A','B'])", "Ghép list thành chuỗi", " - ".join(["A","B"])],

    ["s.strip()", "Xóa khoảng trắng 2 bên", s.strip()],
    ["s.lstrip()", "Xóa khoảng trắng bên trái", s.lstrip()],
    ["s.rstrip()", "Xóa khoảng trắng bên phải", s.rstrip()],

    ["s.startswith('He')", "Bắt đầu bằng 'He'?", s.startswith("He")],
    ["s.endswith('123')", "Kết thúc bằng '123'?", s.endswith("123")],
]

# In bảng kết quả
print(f"{'Hàm':<30} {'Mô tả':<35} {'Kết quả'}")
print("-"*80)
for f, desc, result in functions:
    print(f"{f:<30} {desc:<35} {result}")
