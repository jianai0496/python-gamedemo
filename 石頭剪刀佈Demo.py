# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:08:25 2020

@author: bili_简爱
"""
# 這是一個猜拳的小游戲

import random
import time

# 使用循環來實現運行指定次數
i, win, k = 1, 0, 0

basic_list = ['剪刀', '石頭', '布']

print('''
----------欢迎进入石头剪刀布的小游戏-----------
游戏规则：
1,剪刀能剪坏布，布能能包裹石頭，石頭可能砸坏剪刀
2,直接键入(0~2)之间的一个数字，按回车(Enter)键确认
3,等待电脑做出选择并输出结果
4,一共有三次机会，祝你玩的开心
--------------------end-----------------------
''')

def match_computer(x):
    print(f'电脑此次出{basic_list[x]}了')
    


while i <= 3:
    # 實現玩家的出拳的信息獲取
    print(f'这是您的第{i}次猜测')

    try:
        player = int(input('請玩家輸入此次出拳的信息：[0]剪刀[1]石頭[2]布：'))

    except ValueError:
        print('无效输入,重来')
        continue

    if player >= 3 or player < 0:
        print('超出范围，没关系，重新来过!')
        continue

    # 電腦此次出拳的信息獲取
    computer = random.randint(0, 2)
    # print(computer)

    # 游戲對決，玩家和電腦的出拳信息判斷
    match_computer(computer)
    if (player == 0 and computer == 2)  or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print('恭喜玩家獲勝!')
        win += 1

    elif player == computer:
        print('平局了！恭喜和电脑想到一块去了!')
        k += 1

    else:
        print('玩家失敗,别灰心!')
        
    print('*'*40)

    i += 1

    # 游戏结果判定
    if i == 4:
        print('您的三次机会已用完，等待系统评测......', end='\n')
        print('倒数三个数...')
        for j in range(3, 0, -1):
            time.sleep(1.5)
            print(j)

        if win >= 2 or (k == 2 and win == 1):
            print('恭喜恭喜，玩家获得最终胜利!')

        elif k == 3:
            print('您和电脑平局！')

        else:
            print('本次电脑胜利!')
        print('********Game_Over********')