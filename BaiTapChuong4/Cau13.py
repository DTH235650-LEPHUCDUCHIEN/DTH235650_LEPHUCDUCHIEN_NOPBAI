def tong_uoc_so(n):
    """Hàm tính tổng các ước số của n (không tính n)"""
    if n <= 1:
        return 0
    tong = 1  # luôn có ước số 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  # tránh cộng trùng khi i*i = n
                tong += n // i
    return tong


def la_so_hoan_thien(n):
    return tong_uoc_so(n) == n


def la_so_thinh_vuong(n):
    return tong_uoc_so(n) > n


num = int(input("Nhập số:"))
print(f"{num}:")
print("  Số hoàn thiện?", la_so_hoan_thien(num))
print("  Số thịnh vượng?", la_so_thinh_vuong(num))
