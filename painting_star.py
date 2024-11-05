import turtle

# 初始化画布和海龟
screen = turtle.Screen()
star = turtle.Turtle()

# 设置蓝色背景
screen.bgcolor("blue")

# 设置画笔属性
star.speed(8)  # 设置绘制速度
star.color("yellow", "yellow")  # 设置线条和填充颜色为黄色
star.pensize(2)  # 设置线条粗细

# 开始绘制星星
star.begin_fill()  # 开始填充

# 提起画笔移动到起始位置
star.penup()
star.goto(-50, 0)  # 移动到左侧位置开始绘制
star.pendown()

# 画五角星
for _ in range(5):
    star.forward(100)  # 向前画线
    star.right(144)    # 向右转144度

star.end_fill()  # 结束填充

# 隐藏海龟图标
star.hideturtle()

# 保持窗口打开
screen.mainloop()
