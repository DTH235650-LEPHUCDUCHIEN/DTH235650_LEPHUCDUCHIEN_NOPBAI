print("Chương trinh đếm ngày trong tháng!")
month = int(input("Nhập vào 1 tháng: "))
if month in (1,3,5,7,8,10,12):
    print("Tháng ",month," có 31 ngày.")
elif month in (4,6,9,11):
    print("Tháng ",month," có 30 ngày.")
elif month ==2:
    year = int(input("Mời bạn nhập năm: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Tháng: ",month,"\t",year," có 29 ngày.")
    else:
        print("Tháng: ",month,"\t",year," có 28 ngày.")
else:
<<<<<<< HEAD
   print("Tháng: ",month," không hợp lệ!")
=======
   print("Tháng: ",month," không hợp lệ!")
>>>>>>> 4d7ada004f0e82736f2e4b2f17169d3257014926
