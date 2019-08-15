#Ken Riordan
#week 5 Homework
################################################

import cs112_s17_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Autograded Exercises
#################################################

def bestQuiz(a):
    quizHigh = 0 #placeholder high score
    bestQuiz = -1 #set to -1 so if it doesn't change can return None
    students = len(a) #number of students
    quizzes = len(a[0]) #number of quizzes
    for quiz in range(quizzes): #go through each quiz
        quizList = [a[i][quiz] for i in range(students)] #create list of scores for given quiz
        quizTot = quizCount = 0
        for score in quizList:
            if score >= 0: #if the score is not -1
                quizTot += score #add it to the total
                quizCount += 1 #and add 1 to count
        if quizCount == 0: continue #if no scores exist, skip to next quiz
        else:
            quizAve = quizTot/quizCount #find average for quiz
            if quizAve > quizHigh: #if it's higher than previous...
                quizHigh = quizAve #make note of it
                bestQuiz = quiz #and store quiz number
    if bestQuiz == -1: return None
    else: return bestQuiz

def findNextLocation(a,n):
    #take 2D list (a) and number (n) and find it's [row][col]
    rowIndex = 0 #arbitrary initial assignemnts
    colIndex = 0
    rows = range(len(a)) #get rows
    cols = range(len(a[0])) #get columns, assume square 2D list
    for row in rows:
        for col in cols:
            if a[row][col] == n: #if cell contians n
                rowIndex = row #set indeces to current row and col and return
                colIndex = col
                break
    return (rowIndex,colIndex)

def isKingsTour(board):
    moves = len(board)**2
    for move in range(1,moves): #check each number from 1 to n^2
        #get initial position
        (startRow,startCol) = findNextLocation(board,move)
        #then get position of next move
        (nextRow,nextCol) = findNextLocation(board,move+1)
        if nextRow == startRow: #if rows are the same
            if abs(nextCol - startCol) != 1: #verify movement of 1 in column
                return False
                break
        elif nextCol == startCol: #else if column is the same
            if abs(nextRow - startRow) != 1: #verify movement of 1 in row
                return False
                break
        #else check if distance equals sqrt(2) (1 in 1 direction, on in other)
        elif math.sqrt((startRow-nextRow)**2 + (startCol-nextCol)**2) != math.sqrt(2):
            return False
            break
    return True

#################################################
# Test Functions

def testBestQuiz():
    print("Testing bestQuiz()...", end="")
    a = [ [ 88,  80, 91 ],
        [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    a = [ [ 88,  80, 80 ],
            [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88,  -1, -1 ],
        [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1,  -1, -1 ],
        [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    board =   [[3,2,1],[6,4,9],[5,7,8]]
    assert(isKingsTour(board)==True)
    board =   [[1,2,3],[7,4,8],[6,5,9]]
    assert(isKingsTour(board)==False)
    board =   [[3,2,1],[6,4,0],[5,7,8]]
    assert(isKingsTour(board)==False)
    board =   [[1,14,15,16],
      [ 13,2,7,6],
      [ 12,8,3,5],
      [ 11,10,9,4]]
    assert(isKingsTour(board)==True)
    print("Passed!")

#################################################
#ignore_rest
#################################################

def init(data):
    data.boardNumbers = [] #create 2D list of -1's for initial board
    for row in range(data.rows):
        data.boardNumbers += [[-1]*data.cols]
    data.playerMove = [] #create 2D list to keep track of what player made move in specific cell
    for row in range(data.rows):
        data.playerMove += [[0]*data.cols]
    data.margin = 50 #margin of 50 pixels from
    data.boardWidth = data.width - 2 * data.margin #board is width of window - margin on each side
    data.boardHeight = data.height - 2 * data.margin #and height of window - margins
    data.cellWidth = int(data.boardWidth/data.cols) #each cell is
    data.cellHeight = int(data.boardHeight/data.rows)
    data.markerTop = data.margin
    data.markerLeft = data.margin
    data.number = -1
    data.markerColIndex = 0
    data.markerRowIndex = 0
    data.turn = 1
    data.markerColor = ['','lightBlue','orange']
    data.textColor = ['','darkBlue','darkorange']
    data.turnSum = 0
    data.p1BestTurn = 0
    data.p2BestTurn = 0
    data.p1Score = 0
    data.p2Score = 0
    data.roundOver = False
    data.gameOver = False
    data.roundWinner = 0
    data.gameWinner = 0
    data.results = ['It\'s a Tie, both players awarded 1 point',
            'Player 1 wins the round','Player 2 wins the round']

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (data.gameOver): pass
    else:
        if (event.keysym == "Left"):
            moveMarkerLeft(data)
        elif (event.keysym == "Right"):
            moveMarkerRight(data)
        elif (event.keysym == "Up"):
            moveMarkerUp(data)
        elif (event.keysym == "Down"):
            moveMarkerDown(data)
        #getDigits
        if event.char.isdigit():
            data.number = int(event.char)
            editBoardNumbers(data)
            if not (data.roundOver):
                turnSum(data)
                if data.turn == 1:
                    if data.turnSum > data.p1BestTurn:
                        data.p1BestTurn = data.turnSum
                    playGame(data)
                    data.turn = 2
                else:
                    if data.turnSum > data.p2BestTurn:
                        data.p2BestTurn = data.turnSum
                    playGame(data)
                    data.turn = 1
        if event.keysym == 'Return':
            if data.roundOver == True: roundReset(data)

def moveMarkerLeft(data):
    if data.markerLeft == data.margin: #if it is on leftmost cell, set left side on last cell
        data.markerLeft = data.margin + ((data.cols-1)*data.cellWidth)
    else:
        data.markerLeft -= data.cellWidth

def moveMarkerRight(data):
    #reverse logic of moveMarkerLeft
    if data.markerLeft == data.margin + ((data.cols-1)*data.cellWidth):
        data.markerLeft = data.margin
    else:
        data.markerLeft += data.cellWidth

def moveMarkerDown(data):
    #if top of marker is on top of last row, move to top of top row
    if data.markerTop == data.margin + ((data.rows - 1)*data.cellHeight):
        data.markerTop  = data.margin
    else:
        data.markerTop += data.cellHeight

def moveMarkerUp(data):
    #reverse logic of moveMarkerDown
    if data.markerTop == data.margin:
        data.markerTop = data.margin + ((data.rows - 1)*data.cellHeight)
    else:
        data.markerTop -= data.cellHeight

def timerFired(data):
    pass

def drawGrid(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            topLeftXC = data.margin + (col*data.cellWidth)
            topLeftYC = data.margin + (row*data.cellHeight)
            bottomRightXC = topLeftXC + data.cellWidth
            bottomRightYC = topLeftYC + data.cellHeight
            canvas.create_rectangle(topLeftXC,topLeftYC,bottomRightXC,bottomRightYC)

def getMarkerIndex(data):
    data.markerColIndex = data.markerLeft//data.cellWidth
    data.markerRowIndex = data.markerTop//data.cellHeight
    return (data.markerColIndex,data.markerRowIndex)

def editBoardNumbers(data):
    (col,row) = getMarkerIndex(data)
    if data.boardNumbers[row][col] == -1:
        data.boardNumbers[row][col] = data.number
        data.playerMove[row][col] = data.turn
    elif data.boardNumbers[row][col] != -1 and data.turn == 1:
        data.roundOver = True
        data.roundWinner = 2
        data.p2Score += 1
    elif data.boardNumbers[row][col] != -1 and data.turn == 2:
        data.roundOver = True
        data.roundWinner = 1
        data.p1Score += 1

def turnSum(data):
    data.turnSum = 0
    (col,row) = getMarkerIndex(data)
    if col != 0: colStart = col - 1
    else: colStart = 0
    if row != 0: rowStart = row - 1
    else: rowStart = 0
    if col != data.cols-1: colEnd = col + 1
    else: colEnd = data.cols-1
    if row != data.rows-1: rowEnd = row + 1
    else: rowEnd = data.rows-1
    for r in range(rowStart,rowEnd + 1):
        for c in range(colStart, colEnd + 1):
            if data.boardNumbers[r][c] != -1:
                data.turnSum += data.boardNumbers[r][c]
    return data.turnSum

def boardFull(data): #check to see if board has open spaces
    count = 0 #count the -1's (empty cells) in the board
    for r in range(data.rows):
        for c in range(data.cols):
            if data.boardNumbers[r][c] == -1:
                count += 1
    if count == 0: #if there are no -1's board is full
        return True
    else: return False

def playGame(data):
    data.roundOver = False
    if data.p1BestTurn == 42:
        data.roundOver = True
        data.roundWinner = 1
        data.p1Score += 1
    elif data.p2BestTurn == 42:
        data.roundOver = True
        data.roundWinner = 2
        data.p2Score += 1
    if (boardFull(data)):
        p1 = abs(42-data.p1BestTurn)
        p2 = abs(42-data.p2BestTurn)
        data.roundOver = True
        if p1 == p2:
            data.roundWinner = 0
            data.p1Score += 1
            data.p2Score += 1
        elif p1 < p2:
            data.roundWinner = 1
            data.p1Score += 1
        else:
            data.roundWinner = 2
            data.p2Score += 1
    if data.p1Score == 5:
        data.gameOver = True
        data.gameWinner = 1
    elif data.p2Score == 5:
        data.gameOver = True
        data.gameWinner = 2

def roundReset(data):
    data.boardNumbers = []
    for row in range(data.rows):
        data.boardNumbers += [[-1]*data.cols]
    data.margin = 50
    data.number = -1
    data.markerColIndex = 0
    data.markerRowIndex = 0
    data.turn = 1
    data.markerColor = ['','lightBlue','orange']
    data.textColor = ['','darkBlue','darkorange']
    data.turnSum = 0
    data.p1BestTurn = 0
    data.p2BestTurn = 0
    data.roundOver = False

def redrawAll(canvas, data):
    #draw grid
    drawGrid(canvas, data)
    #display winner if game over
    if (data.gameOver):
        canvas.create_text(data.width*.5,data.height*.5,
                text="Player %d wins the game!" %data.gameWinner,
                fill='red', font='Helvetic 30 bold')
    #display winner if round over
    elif (data.roundOver):
        canvas.create_text(data.width*.5,data.height*.5,
                text="%s.\nHit Return key to start next round"
                %data.results[data.roundWinner],fill='red', font='Helvetic 30 bold')
    #draw highlighted marker
    canvas.create_rectangle(data.markerLeft,data.markerTop,
            data.markerLeft + data.cellWidth,data.markerTop +
                    data.cellHeight,fill=data.markerColor[data.turn])
    #draw game scores for player 1 and 2 respectively
    canvas.create_text(data.width*.25,data.margin*.5,
            text='Player 1: %d'%data.p1Score, fill=data.textColor[1], font = 'Helvetic 10 bold')
    canvas.create_text(data.width*.75,data.margin*.5,
            text='Player 2: %d'%data.p2Score, fill=data.textColor[2], font='Helvetic 10 bold')
    #draw high score for each player for current round
    canvas.create_text(data.width*.25,data.height-data.margin*.5,
            text='Player 1s best turn=%d'%data.p1BestTurn, fill=data.textColor[1], font = 'Helvetic 10')
    canvas.create_text(data.width*.75,data.height-data.margin*.5,
            text='Player 2s best turn=%d'%data.p2BestTurn, fill=data.textColor[2], font='Helvetic 10')
    #draw digit if hit
    (col,row) = getMarkerIndex(data)
    yC = data.margin + data.cellHeight*(.5+row) #y-coordinate of where to center text
    xC = data.margin + data.cellWidth*(.5+col) #x-coord of center of text
    number = data.boardNumbers[row][col]
    color = data.textColor[data.playerMove[row][col]]
    if number != -1:
            canvas.create_text(xC,yC,text=number,fill=color,font='Helvetic 14 bold')



####################################
# use the run function as-is
####################################

def run(rows,cols,width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        1(col,row) = getMarkerIndex(data)
        for row in range(data.rows):
            yC = data.margin + data.cellHeight*(.5+row) #y-coordinate of where to center text
            for col in range(data.cols):
                xC = data.margin + data.cellWidth*(.5+col) #x-coord of center of text
                number = data.boardNumbers[row][col]
                color = data.textColor[data.playerMove[row][col]]
                if number != -1:
                    canvas.create_text(xC,yC,text=number,fill=color,font='Helvetic 14 bold')
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
    data.rows = rows
    data.cols = cols
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



def playGame42(rows,cols):
    run(rows, cols,800,800)



#################################################
# testAll and main
#################################################
def testAll():
    #testBestQuiz()
    #testIsKingsTour()
    playGame42(5,5)

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,repr' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    #cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
