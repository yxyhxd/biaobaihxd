# -*- coding: utf-8 -*- 
# @Time : 2022/2/19 21:01 
# @Author : 雨晨 
# @File : 小爱心.py
'''turtle.setup(width,height,startx,starty)   --创建一个可视化屏幕，width表示宽，height表示高，startx表示左边框距离屏幕左边距离，starty表示上边框距离屏幕上边距离
turtle.pendown()       --落笔，即画笔移动会有痕迹
turtle.penup()         --抬笔，即画笔移动不再有痕迹
turtle.pensize(数值)   -- ?的粗细
turtle.pencolor(颜色)  --?的颜色
turtle.circle(x,y)     --该函数可绘制圆，有两个参数，x代表半径，y代表角度，默认画笔处左侧水平距离x处为原点，y可不写，默认360(整个圆)
turtlr.goto(x,y)       --画笔从当前位置到坐标为（x，y）处
turtle.left(angle)
turtle.right(angle)     --向左或者向右转角度，即调整画笔的方向
坐标说明：可视化屏幕的左上角代表(原点0，0)
这里只是简单的说明一些用到的函数，具体学习请自行搜索。'''
import turtle as a
#我们给海归这个库定义一个名字 a

a.setup(600,500)
#画一个窗口
a.pencolor('red')
#画笔的颜色
a.pensize(2)
#大小
a.penup()
a.goto(0,60)
a.begin_fill()
a.fillcolor('red')
#填充的颜色
a.pendown()
a.left(135)
a.circle(42.3,180)
#角度
a.goto(0,-60)
a.left(90)
a.goto(60,0)
a.circle(42.3,180)
a.end_fill()
a.penup()
a.goto(250,250)

