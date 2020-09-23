import random

answer = random.randint(1,10)
temp = input("猜猜看我现在想的是哪个数字：")
guess = int(temp)
num = 0
while (guess != answer) and (num < 3):
    num = num + 1
    guess = int(temp)
    if answer > guess:
        print("猜小了")
        temp = input("猜错了，请继续猜:")
    else:
        if answer < guess:
            print("猜大了")
            temp = input("猜错了，请继续猜:")
        else:
            print("你猜对了")
print("Game over!")
        
