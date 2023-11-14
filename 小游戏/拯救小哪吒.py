# !/usr/bin/env python
# -*- coding: utf-8 -*-
from maze import Maze
from nezha import Nezha
from controller import Controller
import sys
sys.path.append(r"(C:\Users\阿展要提高\AppData\Local\Programs\Python\Python37\lib\site-packages\maze\__init__.py")

maze_list = [
  [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

Maze(maze_list)

nezha = Nezha(maze_list, 0, 5, 12, 7)

Controller(nezha.go_up, nezha.go_down, nezha.go_left, nezha.go_right)
from turtle import Turtle


class Maze(Turtle):
  size = 20

  def __init__(self, maze_list):
    # 需要先调用父类的初始化方法才能在初始化方法中调用父类的方法
    Turtle.__init__(self)
    self.maze_list = maze_list
    # 为了加快绘图速度隐藏海龟，速度设为最快
    self.hideturtle()
    self.speed(0)
    self.draw_walls()

  def draw_wall(self):
    self.pendown()
    self.begin_fill()
    self.fillcolor('#7392f6')
    for i in range(4):
      self.forward(self.size)
      self.right(90)
    self.end_fill()
    self.penup()

  def draw_walls(self):
    self.penup()
    # 从 (-130, 130) 开始
    self.goto(-130, 130)

    for row in range(13):
      for col in range(13):
        if self.maze_list[row][col] == 1:
          self.draw_wall()
        # 右移一列
        self.goto(self.size * (col + 1) - 130, 130 - self.size * row)
      # 下移一行
      self.goto(-130, 130 - self.size * (row + 1))


from turtle import Turtle


class Nezha(Turtle):
    def __init__(self, maze_list, start_m, start_n, end_m, end_n):
        # 父类初始化
        Turtle.__init__(self)
        self.m = start_m
        self.n = start_n
        self.end_m = end_m
        self.end_n = end_n
        self.maze_list = maze_list
        self.hideturtle()
        self.speed(0)
        self.penup()
        # 移到对应的位置
        self.goto(self.n * 20 - 120, 120 - self.m * 20)
        # 变成海龟
        self.shape('turtle')
        self.color('#28bea0')
        self.setheading(270)
        self.showturtle()
        # 添加哪吒图片作为形状
        screen = self.getscreen()
        screen.addshape('nezha.png')

    def reach_exit(self, m, n):
        if m == self.end_m and n == self.end_n:
            # 变成哪吒
            self.shape('nezha.png')

    def canmove(self, m, n):
        return self.maze_list[m][n] == 0

    def move(self, m, n):
        self.m = m
        self.n = n
        self.goto(self.n * 20 - 120, 120 - self.m * 20)
        self.reach_exit(m, n)

    def go_up(self):
        if self.canmove(self.m - 1, self.n):
            self.setheading(90)
            self.move(self.m - 1, self.n)

    def go_down(self):
        if self.canmove(self.m + 1, self.n):
            self.setheading(270)
            self.move(self.m + 1, self.n)

    def go_left(self):
        if self.canmove(self.m, self.n - 1):
            self.setheading(180)
            self.move(self.m, self.n - 1)

    def go_right(self):
        if self.canmove(self.m, self.n + 1):
            self.setheading(0)
            self.move(self.m, self.n + 1)


from turtle import Turtle


class Controller(Turtle):
    def __init__(self, go_up, go_down, go_left, go_right):
        # 父类初始化
        Turtle.__init__(self)
        # 初始值设置
        self.go_up = go_up
        self.go_down = go_down
        self.go_left = go_left
        self.go_right = go_right
        # 绘制控制器
        self.hideturtle()
        self.speed(0)
        self.draw_btn('上', -15, 165)
        self.draw_btn('下', -15, -135)
        self.draw_btn('左', -165, 15)
        self.draw_btn('右', 135, 15)
        # 绑定点击事件
        screen = self.getscreen()
        screen.onclick(self.handlescreenclick)

    def draw_btn(self, name, x, y):
        self.penup()
        self.goto(x, y)
        self.begin_fill()
        self.fillcolor('#ffffff')
        for i in range(4):
            self.forward(30)
            self.right(90)
        self.end_fill()
        self.color('#000000')
        self.goto(x + 7, y - 20)
        self.write(name, font=('SimHei', 12, 'bold'))

    def handlescreenclick(self, x, y):
        if y > 0 and abs(x) < y:
            self.go_up()
        if y < 0 and abs(x) < -y:
            self.go_down()
        if x < 0 and abs(y) < -x:
            self.go_left()
        if x > 0 and abs(y) < x:
            self.go_right()
