n=4
m=4
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



for i in range(1, n+1, 1):
    print("  " * (n - i) + "* " * i)



m = 7
a= m // 2
for i in range(m):
    for j in range(m):
        if i == j or (j == 0 and i < a) or (j == m - 1 and i >= a):
            print("*", end=' ')
        elif a == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
