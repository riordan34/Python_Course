# lab 6
# Poppa Ken

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.rows = 15 #number of rows
    data.cols = 10 #number of columns
    data.margin = 20 #pxls
    data.cellSize = 50 #Square size of cell in pixels
    data.board = [] #create 2D list of -1's for initial board
    for row in range(data.rows): #create board
        data.board += [['blue']*data.cols]
    data.board[0][0] = "red" # top-left is red
    data.board[0][data.cols-1] = "white" # top-right is white
    data.board[data.rows-1][0] = "green" # bottom-left is green
    data.board[data.rows-1][data.cols-1] = "gray" # bottom-right is gray

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def drawCell(canvas,row,col,data):
    x1 = data.margin+col*data.cellSize
    y1 = data.margin+row*data.cellSize
    x2 = x1 + data.cellSize
    y2 = y1 + data.cellSize
    m = 2 #margin to represent cell outline
    canvas.create_rectangle(x1,y1,x2,y2,fill='black')
    canvas.create_rectangle(x1+m,y1+m,x2+m,y2+m,fill=data.board[row][col])


def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas,row,col,data)

def drawGame(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill='orange')
    drawBoard(canvas,data)

def redrawAll(canvas, data):
    drawGame(canvas,data)
    #drawBoard(canvas,data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

####################################
# playTetris() Function
####################################

def playTetris():
    rows = 15
    cols = 10
    margin = 20 #20 pxl margin
    winWidth = cols*50 + 2*margin #50 pxl squares
    winHeight = rows*50 + 2*margin
    run(winWidth,winHeight)

playTetris()
