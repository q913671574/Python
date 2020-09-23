def factorical(n):
    if n == 1:
        return 1
    else:
        return n * factorical(n - 1)
count = int(input('请输入一个正整数：'))
print('%d 阶乘是：%d ' % ( count , factorical(count)))
