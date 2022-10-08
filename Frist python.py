from re import A
import random
i=0
a=random.randint(1,100)
while i!=100:
    temp=input("猜数字：")
    guess=int(temp)
    if guess==a:
        print("牛逼")
        break
    else:
        if guess>a:
            print("大了")
            i=i+1
        else:
            print("小了")
            i=i+1   

print("游戏结束！")