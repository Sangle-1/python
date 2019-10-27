#!/root/nsd1905/bin/python3     #这里是python的目录
#石头剪刀布小游戏,3局两胜
import random
i = 1            #游戏次数
win = 0        #赢局次数
while i <= 3:
    #1. 提示并获取用户的输入
    player = int(input("请输入 0剪刀 1石头 2布:"))
    
    #2. 让电脑出一个随机数
    computer = random.randint(0,2)
#让用户输入合法
    if player==0 or player==1 or player==2:
        #3. 判断用户的输入,然后显示对应的结果
        if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
            print("第"+str(i)+"局"+"赢了")
            win += 1    
        elif player==computer:
            print("第"+str(i)+"局"+"平局")
        else:
            print("第"+str(i)+"局"+"输了")
        i += 1
    else:
        print("请重新输入合法数字")
#4. 判断最终猜拳结果：3局两胜    
if win >= 2:
    print("恭喜，你赢了！！")
else: 
    print("你输了！！")  
