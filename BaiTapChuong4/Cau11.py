def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range (val, 0, -1):
        s += i
    return s
#Trường hợp 1
def case1():
    print("Trường hợp 1: ")
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())
    print()
#Trường hợp 2
def case2():
    print("Trường hợp 2: ")
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())
    print()
#Trường hợp 3
def case3():
    print("Trường hợp 3: ")
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())
    print()
#Chạy các TH
def main():
    case1()
    case2()
    case3()
#Gọi hàm main
if __name__ == '__main__':
    main()