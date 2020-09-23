def fab(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)

count = int(input('请输入斐波那契数列层数：'))
result = fab(count)
print('计算出的斐波那契数列值为：%d ' % result)
