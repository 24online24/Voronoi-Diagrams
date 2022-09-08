""" Se genereaza Diagrama Voronoi pentru un sistem de n puncte din plan cu modulul graphics.py """

import threading
from numpy import zeros, absolute
from graphics import *
import threading

WIDTH = int(input("Width = "))
HEIGHT = int(input("Height = "))
nrpuncte = int(input("Numar de puncte = "))
X, Y = zeros(nrpuncte), zeros(nrpuncte)
# win1 = GraphWin("Diagrama Voronoi Euclidean", Lung, Inalt)
# win2 = GraphWin("Diagrama Voronoi Manhattan", Lung, Inalt)
colors = ["blue", "black", "brown", "red", "yellow",
          "green", "orange", "magenta", "turquoise", "pink"]


def manhattan_distance(x1, y1, x2, y2):
    return absolute(x2-x1)+absolute(y2-y1)


def euclidian_distance(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2


def voronoi(Lung, Inalt, nrpuncte, X, Y, distance):
    voro = zeros((Inalt, Lung), dtype=int)
    for l in range(0, Inalt):
        for j in range(0, Lung):
            Distmin = distance(l, j, X[0], Y[0])
            voro[l, j] = 0
            for i in range(1, nrpuncte):
                if Distmin > distance(l, j, X[i], Y[i]):
                    Distmin = distance(l, j, X[i], Y[i])
                    voro[l, j] = i
    return voro


def draw(distance):
    win = GraphWin("Diagrama Voronoi Euclidean" + distance.__name__[0], WIDTH, HEIGHT)
    voro = voronoi(WIDTH, HEIGHT, nrpuncte, X, Y, distance)
    for l in range(0, HEIGHT):
        for j in range(0, WIDTH):
            p = Point(l, j)
            p.setOutline(colors[voro[l, j]])
            p.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    for i in range(0, nrpuncte):
        print("X[", i, "]=")
        X[i] = int(input())
        print("Y[", i, "]=")
        Y[i] = int(input())

    threads = []
    threads.append(threading.Thread(target=draw, args=(euclidian_distance,)))
    # threads.append(threading.Thread(target=draw, args=(manhattan_distance,)))

    for t in threads:
        t.start()

    # for t in threads:
    #     t.join()