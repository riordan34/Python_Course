# lab 6
# Poppa Ken

from tkinter import *
import random, copy

####################################
# customize these functions
####################################

def init(data):
    data.rows = 15 #number of rows
    data.cols = 10 #number of columns
    data.margin = 20 #pxls
    data.cellSize = 50 #Square size of cell in pixels
    data.board = [] #create 2D list for initial board
    for row in range(data.rows): #create board
        data.board += [['blue']*data.cols]
    data.board[0][0] = "red" # top-left is red
    data.board[0][data.cols-1] = "white" # top-right is white
    data.board[data.rows-1][0] = "green" # bottom-left is green
    data.board[data.rows-1][data.cols-1] = "gray" # bottom-right is gray
    iPiece = [[True,True,True,True]]
    jPiece = [[True,False,False],[True,True,True]]
    lPiece = [[False,False,True],[True,True,True]]
    oPiece = [[True,True],[True,True]]
    sPiece = [[ False, True, True],[ True, True, False ]]
    tPiece = [[ False, True, False ],[ True,True, True]]
    zPiece = [[ True,  True, False ],[ False,True, True]]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    data.fallingPiece = data.tetrisPieces[0]
    data.fallingPieceColor = data.tetrisPieceColors[0]
    data.fallingPieceRow = 0
    data.fallingPieceCol = data.cols//2 - len(data.fallingPiece[0])//2

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (event.keysym == "Left"):
        moveFallingPiece(data,0,-1)
    elif (event.keysym == "Right"):
        moveFallingPiece(data,0,1)
    elif (event.keysym == "Down"):
        moveFallingPiece(data,1,0)
    elif (event.keysym == "Up"):
        rotateFallingPiece(data)
    else:
    # for now, for testing purposes, just choose a new falling piece
    # whenever non-right/left/down key is pressed!
        newFallingPiece(data)

def timerFired(data):
    pass

def drawCell(canvas,row,col,data,color):
    x1 = data.margin+col*data.cellSize
    y1 = data.margin+row*data.cellSize
    x2 = x1 + data.cellSize
    y2 = y1 + data.cellSize
    m = 2 #margin to represent cell outline
    canvas.create_rectangle(x1,y1,x2,y2,fill='black')
    canvas.create_rectangle(x1+m,y1+m,x2+m,y2+m,fill=color)

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(canvas,row,col,data,color)

def drawFallingPiece(canvas,data):
    r = 0 #index to iterate through piece booleans
    c = 0 #index to iterate through piece booleans
    x1 = data.fallingPieceCol
    y1 = data.fallingPieceRow
    x2 = x1 + len(data.fallingPiece[0])
    y2 = y1 + len(data.fallingPiece)
    for row in range (y1,y2):
        for col in range(x1,x2):
            if (data.fallingPiece[r][c]):
                color = data.fallingPieceColor
                drawCell(canvas,row,col,data,color)
            c += 1
        c = 0 #reset col index for piece
        r += 1 #go to next row

def drawGame(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill='orange')
    drawBoard(canvas,data)
    drawFallingPiece(canvas,data)

def newFallingPiece(data):
    choice = random.randint(0,6)
    data.fallingPiece = data.tetrisPieces[choice]
    data.fallingPieceColor = data.tetrisPieceColors[choice]
    data.fallingPieceRow = 0
    data.fallingPieceCol = data.cols//2 - len(data.fallingPiece[0])//2

def moveFallingPiece(data,drow,dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    if not fallingPieceisLegal(data):
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol

def fallingPieceisLegal(data):
    r = 0 #index to iterate through piece booleans
    c = 0 #index to iterate through piece booleans
    x1 = data.fallingPieceCol
    y1 = data.fallingPieceRow
    x2 = x1 + len(data.fallingPiece[0])
    y2 = y1 + len(data.fallingPiece)
    for row in range (y1,y2):
        for col in range(x1,x2):
            if (data.fallingPiece[r][c]):
                if row < 0 or row >= data.rows:
                    return False
                    break
                elif col < 0 or col >= data.cols:
                    return False
                    break
                elif data.board[row][col] != 'blue':
                    return False
                    break
            c += 1
        c = 0 #reset col index for piece
        r += 1 #go to next row
    return True

def rotateFallingPiece(data):
    initPiece = copy.deepcopy(data.fallingPiece) #store initial piece booleans
    initx1 = data.fallingPieceCol #left col of initial piece
    inity1 = data.fallingPieceRow #top row of initial piece
    initRows = len(data.fallingPiece) #initial piece dimensions
    initCols = len(data.fallingPiece[0])
    cols = initRows #new column dimension is old rows
    rows = initCols #new row dimension is old columns
    oldCenterRow = inity1 + initRows//2 #calculate old center row (top + half height)
    oldCenterCol = initx1 + initCols//2 #old center col (left + half len)
    y1 = oldCenterRow - rows//2 #new top = old center row - half new height (rows)
    x1 = oldCenterCol - cols//2 #new left = old center col - half new length (cols)
    newFallingPiece = [] #create newFallingPiece in correct, rotated, dimensions
    iC = 0 #index for column of initial fallingPiece
    iR = 0 #index for row of initial fallingPiece
    for row in range(rows):
        newFallingPiece += [[False]*cols]
    for row in range(rows): #rotate piece
        for col in range(cols):
            newFallingPiece[row][col] = initPiece[col][initCols -1 - row]
    data.fallingPiece = newFallingPiece
    data.fallingPieceCol = x1 #set new left col and top row
    data.fallingPieceRow = y1
    if not fallingPieceisLegal(data): #if move not legal, reset piece, row and col
        fallingPiece = initPiece
        data.fallingPieceCol = initx1
        data.fallingPieceRow = inity1


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
