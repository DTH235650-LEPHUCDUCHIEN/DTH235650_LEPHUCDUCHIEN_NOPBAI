from datetime import datetime, timedelta


# Hàm tìm ngày kế tiếp
def ngay_ke_tiep(ngay, thang, nam):
    ngay_hien_tai = datetime(nam, thang, ngay)

    # Cộng thêm một ngày (timedelta)
    ngay_tiep_theo = ngay_hien_tai + timedelta(days=1)

    # Trả về ngày kế tiếp dưới định dạng dd/mm/yyyy
    return ngay_tiep_theo.strftime("%d/%m/%Y")


# Nhập vào ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tìm và in ngày kế tiếp
<<<<<<< HEAD
print("Ngày kế tiếp là:", ngay_ke_tiep(ngay, thang, nam))
=======
print("Ngày kế tiếp là:", ngay_ke_tiep(ngay, thang, nam))
>>>>>>> 4d7ada004f0e82736f2e4b2f17169d3257014926
