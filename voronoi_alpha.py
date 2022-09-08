""" Se genereaza Diagrama Voronoi pentru un sistem de n puncte din plan cu modulul graphics.py """

from numpy import zeros
from graphics import *
Lung = int(input("Lungime = "))
Inalt = int(input("Inaltime = "))
nrpuncte=int(input("Numar de puncte = "))
X,Y=zeros(nrpuncte),zeros(nrpuncte)
voro=zeros((Inalt,Lung), dtype=int)
Voro=zeros((Inalt,Lung), dtype=int)
win = GraphWin("Diagrama Voronoi",Lung,Inalt)
culori = ["blue","black","brown","red","yellow","green","orange","magenta","turquoise","pink"]
def distanta2(a,b,x,y):
    return (a-x)**2+(b-y)**2
def voronoi(Lung,Inalt,nrpuncte,X,Y):
    global voro
    for l in range(0,Inalt):
        for j in range(0,Lung):
            Distmin=distanta2(l,j,X[0],Y[0])
            voro[l,j]=0
            for i in range(1,nrpuncte):
                if Distmin>distanta2(l,j,X[i],Y[i]):
                    Distmin=distanta2(l,j,X[i],Y[i])
                    voro[l,j]=i
    return voro
for i in range(0,nrpuncte):
    print("X[",i,"]=")
    X[i]=int(input())
    print("Y[",i,"]=")
    Y[i]=int(input())
Voro = voronoi(Lung,Inalt,nrpuncte,X,Y)
for l in range(0, Inalt):
    for j in range(0, Lung):
        P = Point(l,j)
        P.setOutline(culori[Voro[l,j]])
        P.draw(win)
win.getMouse()
win.close()
