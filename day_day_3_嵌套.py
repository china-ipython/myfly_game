# 石头剪刀步游戏流程编程
import random
player = int(input("请输入1石头，2剪刀，3步 ："))
computer_1 = random.randint(1,3)
if (player == 1 and computer_1 == 2)    or (player == 2 and computer_1 == 3)    or (player == 3 and computer_1 == 1):

    print("太简单了，简直是弱爆了,我出的是%d,电脑出的是%d" %(player,computer_1))
    if player == 1 and computer_1 == 2:
        print("我出的拳头，电脑出的剪刀")
    elif player == 2 and computer_1 == 3:
        print("我出的剪刀，电脑出的步")
    else:
        print("我出的步，电脑出的拳头")
elif player == computer_1:
    print("这一局竟然平局了，表示不服")
elif player != 1 or 2 or 3 :
    print("请输入正确的数字1或者2或者3 ")
else:
    print("我竟然会输，Oh MY God")