x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
s=0
for i in range(1,n+1):
    tu=x**i
    mau=1
    for j in range(1,i+1):
        mau=mau*j
    s=s+(tu/mau)
<<<<<<< HEAD
print("s({0},{1})={2}".format(x,n,s))
=======
print("s({0},{1})={2}".format(x,n,s))
>>>>>>> 4d7ada004f0e82736f2e4b2f17169d3257014926
