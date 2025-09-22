import re

def NegativeNumberInStrings(s: str):
    """
    Hàm tìm và xuất ra tất cả các số nguyên âm trong chuỗi.
    """
    # Tìm tất cả số nguyên âm bằng regex: dấu '-' theo sau là các chữ số
    negatives = re.findall(r"-\d+", s)

    # Chuyển chuỗi số thành kiểu int
    negatives = [int(num) for num in negatives]

    # Xuất kết quả
    if negatives:
        print("Các số nguyên âm trong chuỗi:", negatives)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

x=input("Nhập chuỗi:")
NegativeNumberInStrings(x)
