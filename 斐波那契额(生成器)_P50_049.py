def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a



a = libs()
print(a)
print(a)
print(a)
print(a)
print(a)
print(a)
print(a)



