# futval_graph.py

from graphics import *

def main():

    # Create a graphics window with labels on left edge
    width = 600
    height = 600
    win = GraphWin("Tic Tac Toe", width, height)
    win.setBackground("white")

    # draw grid
    Line(Point(0,height//3),Point(width,height//3)).draw(win)
    Line(Point(0,height//1.5),Point(width,height//1.5)).draw(win)
    Line(Point(width//3,0),Point(width//3,height)).draw(win)
    Line(Point(width//1.5,0),Point(width//1.5,height)).draw(win)

    # keep track of entry for each square (x=1, o = 0)
    # determine which aquare clicked
    # update tracker
    # display appropriate symbol
    # end game if 3 of same symbol in a row

    entries = [[-1 for x in range(3)] for y in range(3)] 
    move = False

    while len(entries) < 9:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        if x < width//3:
            col = 0
        elif x < width//1.5:
            col = 1
        else:
            col = 2

        if y < height//3:
            row = 0
        elif y < width//1.5:
            row = 1
        else:
            row = 2

        # don't update a cell that already has a value
        move = not move
        entries[row][col] = move;

        # display symbol, centered in the cell
        cp = Point(col*width//3 + 100, row*height//3 + 100)
        if move:    # display X
            label = Text(cp,"X")
        else:       # display O
            label = Text(cp,"0")

        label.setSize(36)
        label.draw(win)

        # if 3 of same in a row, col, or diagonal draw line 
        # check row
        for i in range(3):
            if entries[row][i] != move:
                break
            elif i == 2:
                print("game over")
        
        # check col
        for i in range(3):
            if entries[i][col] != move:
                break
            elif i == 2:
                print("game over")

        # check both diagonals        
        if entries[0][0] == move and entries[1][1] == move and entries[2][2] == move:
            print("game over")
        elif entries[0][2] == move and entries[1][1] == move and entries[2][0] == move:
            print("game over")

    input("Press <Enter> to quit")
    win.close()

main()
