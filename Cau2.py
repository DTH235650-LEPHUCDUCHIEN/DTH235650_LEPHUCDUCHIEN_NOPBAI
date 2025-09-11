<<<<<<< HEAD
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
   print("Tháng: ",month," không hợp lệ!")
=======
print('Hello world')

print('Albert Einstein đã từng nói: Một người không bao giờ mắc sai lầm không bao giờ thử bất kỳ điều gì mới.')

if 5 > 2:
    print('Five is greater than two!')

total = 1 + \
2 + \
3
print(total); print('Hello Python!')

if True:
    print('True')
else:
    print('False')

#This is a comment
print('Hello, World!')
>>>>>>> c0de2ac0eb83faaf12050d954f3f6ef691c199bb
