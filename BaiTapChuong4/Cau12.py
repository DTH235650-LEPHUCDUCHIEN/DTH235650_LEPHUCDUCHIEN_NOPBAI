def oscillate(start, stop):
    # Dao động từ start đến 0
    for i in range(abs(start), -1, -1):
        yield -i
        if i != 0:
            yield i

    # Dao động từ 0 đến stop - 1
    for i in range(1, stop):
        yield i
        yield -i

# Gọi hàm và in kết quả
for n in oscillate(-3, 5):
    print(n, end=' ')
print()