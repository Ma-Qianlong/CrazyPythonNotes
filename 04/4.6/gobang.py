#!/usr/bin/env python

# -*- *************** -*-
# @File  : gobang.py
# @Description : 控制台五子棋
# @Author: mql
# @Time  : 2020/1/9 23:26
# -*- *************** -*-

import  random

# 定义棋盘大小
BOARD_SIZE = 15
# 定义一个全局的二维数组来充当棋盘
board = []
# 无字
point_no = "+"
# 电脑落子
point_pc = "○"
# 玩家落子
point_user = "●"

pp = ['0', '①', '②', '③', '④', \
      '⑤', '⑥', '⑦', '⑧', '⑨', \
      '⑩', '⑪', '⑫', '⑬', '⑭']  # , '⑮']


def initBoard():
    # 画出棋盘(初始化棋盘数据)
    for i in range(BOARD_SIZE):
        row = [point_no] * BOARD_SIZE
        board.append(row)


def printBoard():
    for i in range(-1, BOARD_SIZE):
        for j in range(-1, BOARD_SIZE):
            if i == -1 and j == -1:
                print(' ', end=" ")
            elif i == -1 and j > -1:
                if j > 0 and (j % 2 == 0):
                    print("%s]" % j, end="")
                elif j > 10:
                    print("%s" % pp[j], end="")
                else:
                    print("[%s" % pp[j], end="")
            elif j == -1 and i > -1:
                print("%s" % pp[i], end=" ")
            else:
                print(board[i][j], end=" ")
        print()

def pc_doPoint():
    pc_x = random.randint(0, 14)
    pc_y = random.randint(0, 14)
    while board[pc_x][pc_y] != point_no:
        pc_x = random.randint(0, 14)
        pc_y = random.randint(0, 14)
    board[pc_x][pc_y] = point_pc

def whoWin(the_point):
    ccCount = 0
    lastEq = False
    # x 方向
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if ccCount==0 and board[x][y] == the_point:
                lastEq = True
                ccCount += 1
            elif lastEq and board[x][y] == the_point:
                ccCount += 1
                if ccCount == 5:
                    break
            else:
                lastEq = False
                ccCount = 0
        if ccCount == 5:
            return True
        else:
            ccCount = 0
            lastEq = False

initBoard()
printBoard()

inputStr = input("请输入您要落子的坐标，应以x,y的格式：\n")
while inputStr != None:
    x_str, y_str = inputStr.split(sep=",")
    x = int(x_str)
    y = int(y_str)
    if(x<0 or x>15 or y < 0 or y > 15):
        inputStr = input("落子的坐标范围应为0到14！请重新输入")
        continue

    board[int(x_str)][int(y_str)] = point_user
    '''
    电脑随机生成两个整数，作为电脑下棋的坐标 ， 赋值给 board 列表
    还涉及
        1. 坐标的有效性，只能是数字，不能超出棋盘范围
        2 . 下的棋的点，不能重复下棋
        3. 每次下棋后，需要扫描谁赢了
    '''
    pc_doPoint()

    if whoWin(point_user):
        print("Game Over, You Win!!!")
        break
    elif whoWin(point_pc):
        print("Game Over, PC Win!!!")
        break
    printBoard()
    inputStr = input("请输入您要落子的坐标，应以x,y的格式：\n")
