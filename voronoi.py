""" Se genereaza Diagrama Voronoi pentru un sistem de n puncte din plan cu modulul graphics.py """

from numpy import zeros, absolute
from graphics import *
from random import randint

WIDTH = int(input("Width = "))
HEIGHT = int(input("Height = "))
points = int(input("Number of points = "))
x, y = zeros(points), zeros(points)
win_euc = GraphWin("Euclidean Distance Voronoi Diagram", WIDTH, HEIGHT, autoflush=False)
win_man = GraphWin("Manhattan Distance Voronoi Diagram", WIDTH, HEIGHT, autoflush=False)
colors = ["blue", "black", "brown", "red", "yellow",
          "green", "orange", "magenta", "turquoise", "pink"]


def manhattan_distance(x1, y1, x2, y2):
    return absolute(x2-x1)+absolute(y2-y1)


def euclidian_distance(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2


def voronoi(width, height, nrpuncte, x, y, distance):
    voro = zeros((height, width), dtype=int)
    for l in range(0, height):
        for j in range(0, width):
            min_distance = distance(l, j, x[0], y[0])
            voro[l, j] = 0
            for i in range(1, nrpuncte):
                if min_distance > distance(l, j, x[i], y[i]):
                    min_distance = distance(l, j, x[i], y[i])
                    voro[l, j] = i
    return voro


def draw_lines(win: GraphWin):
    for i in range(0, points):
        line1 = Line(Point(x[i] - 4, y[i] - 4), Point(x[i] + 5, y[i] + 5))
        line1.setOutline("white")
        line2 = Line(Point(x[i] - 4, y[i] + 4), Point(x[i] + 5, y[i] - 5))
        line2.setOutline("white")
        line1.draw(win)
        line2.draw(win)

def draw():
    voro_euc = voronoi(WIDTH, HEIGHT, points, x, y, euclidian_distance)
    voro_man = voronoi(WIDTH, HEIGHT, points, x, y, manhattan_distance)
    for l in range(0, HEIGHT):
        for j in range(0, WIDTH):
            p1 = Point(l, j)
            p1.setOutline(colors[voro_euc[l, j]])
            p1.draw(win_euc)
            p2 = Point(l, j)
            p2.setOutline(colors[voro_man[l, j]])
            p2.draw(win_man)
    draw_lines(win_euc)
    draw_lines(win_man)
    win_euc.flush()
    win_man.flush()
    win_euc.getMouse()
    win_euc.close()
    win_man.getMouse()
    win_man.close()


if __name__ == '__main__':
    for i in range(0, points):
        # print("X[{}]=".format(i), end = '')
        # x[i] = int(input())
        # print("Y[{}]=".format(i), end = '')
        # y[i] = int(input())
        x[i] = randint(0, WIDTH)
        y[i] = randint(0, HEIGHT)
    draw()
