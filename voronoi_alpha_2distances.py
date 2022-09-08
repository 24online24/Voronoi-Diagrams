""" Se genereaza Diagrama Voronoi pentru un sistem de n puncte din plan cu modulul graphics.py """

from numpy import zeros, absolute
from graphics import *
Lung = int(input("Lungime = "))
Inalt = int(input("Inaltime = "))
nrpuncte = int(input("Numar de puncte = "))
X, Y = zeros(nrpuncte), zeros(nrpuncte)
win1 = GraphWin("Diagrama Voronoi Euclidean", Lung, Inalt)
win2 = GraphWin("Diagrama Voronoi Manhattan", Lung, Inalt)
culori = ["blue", "black", "brown", "red", "yellow",
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
            of.write(str(l) + ' ' + str(j) + ' ' + str(X[0]) + ' ' +str(Y[0]) + ' ' + str(Distmin) + '\n')
            voro[l, j] = 0
            for i in range(1, nrpuncte):
                of.write(str(l) + ' ' + str(j) + ' ' + str(X[i]) + ' ' + str(Y[i]) + ' ' + str(distance(l, j, X[i], Y[i])) + '\n' + '\n')
                if Distmin > distance(l, j, X[i], Y[i]):
                    Distmin = distance(l, j, X[i], Y[i])
                    voro[l, j] = i
    return voro

of = open('output.txt', 'w')
for i in range(0, nrpuncte):
    print("X[", i, "]=")
    X[i] = int(input())
    print("Y[", i, "]=")
    Y[i] = int(input())

voro_euclidean = voronoi(Lung, Inalt, nrpuncte, X, Y, euclidian_distance)
voro_manhattan = voronoi(Lung, Inalt, nrpuncte, X, Y, manhattan_distance)
of.close()
for l in range(0, Inalt):
    for j in range(0, Lung):
        p1 = Point(l, j)
        p1.setOutline(culori[voro_euclidean[l, j]])
        p1.draw(win1)
        p2 = Point(l, j)
        p2.setOutline(culori[voro_manhattan[l, j]])
        p2.draw(win2)
win1.getMouse()
win1.close()
win2.getMouse()
win2.close()
