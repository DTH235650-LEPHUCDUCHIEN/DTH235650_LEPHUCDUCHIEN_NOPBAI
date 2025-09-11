print("Chuong trình kiểm tra năm nhuần!")
year = int (input("Mời thím nhập vào một năm: "))
if( year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("Năm ",year," là năm nhuần.")
else:
    print("Năm ",year," là năm không nhuần.")