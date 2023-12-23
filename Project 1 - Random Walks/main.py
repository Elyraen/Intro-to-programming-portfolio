import random
from graphics import *

def main():
    win = GraphWin('Project 1', 800, 600)

    current = Point(399,299)
    current.draw(win)
    stepChoice = [-2, 2]

    rect = Rectangle(Point(199,99), Point(599,499))
    rect.draw(win)

    for i in range(10000):
        dx = random.choice(stepChoice)
        dy = random.choice(stepChoice)

        if current.getX()+dx<=599 and current.getX()+dx>=199 and current.getY()+dy<=499 and current.getY()+dy>=99:
            nextPt=Point(current.getX()+dx,current.getY()+dy)
            line=Line(current,nextPt)
            line.draw(win)
            current = nextPt

    win.getMouse()
    win.close()

main()






"""
currentInt = 0
    for i in range(200):
        print(currentInt, end=", ") #end=", "
        choiceList = [-1,1]
        dx = random.choice(choiceList)
        if currentInt + dx < 6 and currentInt + dx > -6:
            currentInt = currentInt + dx
"""