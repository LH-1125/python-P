# Craps赌博游戏.py
import random  # 导入随机数模块
import time  # 导入时间模块

money = 1000  # 玩家初始资金
while money > 0:  # 当玩家资金大于0时，游戏继续
    print(f'你的总资产为: {money}元')  # 打印玩家当前总资产

    while True:  # 循环直到玩家下注金额有效
        debt = int(input('请下注: '))  # 提示玩家下注并获取输入
        if 0 < debt <= money:  # 判断下注金额是否在有效范围内
            break  # 如果下注金额有效，跳出循环
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = int(random.randrange(1, 7)) + int(random.randrange(1, 7))
    # 模拟第一次摇骰子，生成两个1-6的随机数并相加
    print(f'\n玩家摇出了{first_point}点')  # 打印玩家第一次摇出的点数
    if first_point == 7 or first_point == 11: # 如果第一次摇出的点数为7或11，玩家获胜
        time.sleep(2)  # 暂停2秒
        print('玩家胜!\n')  # 打印玩家获胜信息
        money += debt  # 玩家资金增加下注金额
    elif first_point == 2 or first_point == 3 or first_point == 12:  # 如果第一次摇出的点数为2、3或12，庄家获胜
        time.sleep(2)  # 暂停2秒
        print('庄家胜!\n')  # 打印庄家获胜信息
        money -= debt  # 玩家资金减少下注金额
    else:  # 如果第一次摇出的点数既不是获胜也不是失败的点数，进入下一轮
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:  # 循环直到分出胜负
            current_point = random.randrange(1, 7) + random.randrange(1, 7)  # 模拟后续摇骰子
            time.sleep(2)  # 暂停2秒
            print(f'玩家摇出了{current_point}点')  # 打印玩家本次摇出的点数
            if current_point == 7:  # 如果本次摇出的点数为7，庄家获胜
                time.sleep(2)  # 暂停2秒
                print('庄家胜!\n')  # 打印庄家获胜信息
                money -= debt  # 玩家资金减少下注金额
                break  # 跳出当前循环
            elif current_point == first_point:  # 如果本次摇出的点数与第一次摇出的点数相同，玩家获胜
                time.sleep(2)  # 暂停2秒
                print('玩家胜!\n')  # 打印玩家获胜信息
                money += debt  # 玩家资金增加下注金额
                break  # 跳出当前循环
time.sleep(2)  # 暂停1秒
print('你破产了, 游戏结束!')  # 当玩家资金小于等于0时，打印破产信息，游戏结束