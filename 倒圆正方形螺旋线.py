#倒圆正方形螺旋线.py
from turtle import * # 从 turtle 模块导入所有函数和类

setup(1000, 500, 100, 100)  # 设置绘图窗口的大小和位置 (宽度, 高度, 窗口左上角 x 坐标, 窗口左上角 y 坐标)

penup()  # 抬起画笔，移动时不绘制
goto(-100, -100)  # 将海龟移动到坐标 (-100, -100)，作为起始绘制位置
pendown()  # 放下画笔，开始绘制
pensize(1)  # 设置画笔的粗细为 1 像素
pencolor("Orange")  # 设置画笔的颜色为橙色
seth(0)  # 设置海龟的朝向为 0 度（正东方向）

side_length = 200  # 初始化变量 side_length 为 200，表示初始直线段的长度
reduction = 4  # 初始化变量 reduction 为 4，表示每次绘制后直线段长度减少的量
radius = 10  # 初始化变量 radius 为 10，表示圆角的半径

for _ in range(60):  # 开始一个循环，执行 60 次
    # 直线段
    speed(1)  # 设置绘制直线段的速度为最慢 (1)
    forward(side_length - 2 * radius)  # 向前移动 side_length 减去两个圆角半径的距离，绘制直线段

    # 圆角（四分之一圆弧）
    speed(10)  # 设置绘制圆弧的速度为最快 (10)
    circle(radius, 90)  # 绘制一个半径为 radius，角度为 90 度的圆弧（四分之一圆）

    side_length -= reduction  # 将 side_length 减去 reduction，为下一次绘制缩短直线段
    if side_length <= 2 * radius:  # 如果当前的 side_length 小于或等于两倍的半径，则停止循环
        break

speed(10)  # 设置绘制圆点的速度为最快 (10)
dot(5, "Red")  # 在海龟当前位置绘制一个直径为 5 像素的红色圆点
done()  # 保持绘图窗口打开，直到手动关闭



