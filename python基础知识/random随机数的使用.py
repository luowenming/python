import random

#玩家
player = int(input('请输入您要出的东西 石头（1）剪刀（2）布（3）'))
#电脑
computer = random.randint(1,3)

if player == 1 and computer == 2:
    print('玩家胜,%d:%d' % (player, computer))
elif player == 2 and computer == 3:
    print('玩家胜,%d:%d' % (player, computer))
elif player == 3 and computer == 1:
    print('玩家胜,%d:%d' % (player, computer))
elif player == computer:
    print('平局,%d:%d' % (player, computer))
else:
    print('电脑胜,%d:%d' % (player, computer))