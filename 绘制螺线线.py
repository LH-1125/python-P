# 绘制螺线线.py
import matplotlib.pyplot as plt #matplotlib.pyplot 是一个用于绘制图表的库，通常简写为 plt。它提供了创建各种静态、动态和交互式图表的函数。
import numpy as np #numpy 是一个用于进行数值计算的库，它提供了高效的多维数组对象和用于处理这些数组的工具。通常简写为 np

def spiral_slow(turns, points_per_turn, start_radius, radius_increment, delay):
    #这段代码定义了一个名为 spiral_slow 的函数。
    """
    生成并缓慢绘制螺旋线的 x 和 y 坐标。

    Args:
        turns (int): 螺旋的圈数。
        points_per_turn (int): 每圈的点数。
        start_radius (float): 起始半径。
        radius_increment (float): 每圈半径的增量。
        delay (float): 每次绘制后的延迟时间（秒）。
    """
    theta = np.linspace(0, 2 * np.pi * turns, turns * points_per_turn)
    # 生成角度数组，从 0 到 2*pi*turns，包含 turns * points_per_turn 个点
    radius = start_radius + radius_increment * theta / (2 * np.pi)
    # 计算每个角度对应的半径，半径随着角度的增加而线性增加
    x = radius * np.cos(theta) # 计算每个点的 x 坐标
    y = radius * np.sin(theta) # 计算每个点的 y 坐标

    plt.figure(figsize=(8, 8)) # 创建一个 8x8 英寸的图形
    plt.title("Slowly drawn spiral") # 设置图表的标题
    plt.xlabel("X-axis") # 设置 x 轴的标签
    plt.ylabel("Y-axis") # 设置 y 轴的标签
    plt.grid(True) # 显示网格线
    plt.axhline(0, color='black', linewidth=0.5) # 绘制一条水平的黑线作为 x 轴
    plt.axvline(0, color='black', linewidth=0.5) # 绘制一条垂直的黑线作为 y 轴
    plt.gca().set_aspect('equal', adjustable='box') # 设置坐标轴的纵横比相等

    for i in range(len(x)): # 遍历所有的点
        plt.plot(x[:i+1], y[:i+1], 'r:')  # 绘制从起点到当前点的红色点线
        plt.draw()                         # 强制重绘图形
        plt.pause(delay)                   # 暂停一段时间，实现缓慢绘制的效果

    plt.show() # 显示绘制的图形

if __name__ == "__main__":
    # 设置螺旋线的参数
    turns = 5 # 螺旋的圈数为 5
    points_per_turn = 60 # 每圈包含 60 个点
    start_radius = 0.5 # 起始半径为 0.5
    radius_increment = 0.25 # 每圈半径增加 0.25
    delay = 0.000000000000001       # 设置延迟时间为 0.000000000000001 秒

    # 缓慢绘制螺旋线
    spiral_slow(turns, points_per_turn, start_radius, radius_increment, delay)