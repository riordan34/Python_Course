#Hw7
#Poppa K
# Barebones timer, mouse, and keyboard events

import math
import random
from tkinter import *

####################################
#Helper Functions
####################################

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

def IsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

####################################
#part 5: select problems from week1-5 practice
####################################

def nearestBustStop(street):
    closest = 0
    distance = street%8
    if (distance < 5):
        closest = street - distance
    else:
        closest = street + (8 - distance)
    return closest

def rotated(n):
    #rotate number one digit right
    power = int(math.log(n,10))
    lastDigit = n%10
    newFirstDigit = lastDigit * (10**power)
    rotated = int(n/10) + newFirstDigit
    return rotated

def isCircularPrime(n):
    if not (IsPrime(n)):
        return False
    initN = n
    n = rotated(n)
    while (initN != n): #go around necessary number of rotations
        if IsPrime(n):
            n = rotated(n)
        else:
            return False
            break
    return True

def nthCircularPrime(n):
    found = 0
    guess = 0
    while (found < n):
        guess += 1
        if isCircularPrime(guess):
            found += 1
    return guess

def replace(s1,s2,s3):
    newString = ''
    chars = len(s2)
    i = 0
    while (i < len(s1)-chars):
        if s1[i:i+chars] == s2:
            newString += s3
            i += chars
        else:
            newString += s1[i]
            i += 1
    if s1[i:] == s2:
        newString += s3
    else: newString += s1[i:]
    return newString

def join(L,delim):
    s = ''
    for entry in range(len(L)):
        s += L[entry]
        if entry < len(L)-1: #add delim if not last entry
            s += delim
    return s

def f(x):
    return x**2-1


def map(f,a):
    results = []
    for entry in a:
        ans =f(entry)
        results.append(ans)
    return results


####################################
# customize these functions
####################################

def init(data):
    data.rows = int(data.width/100*3) #12 with width of 400 pxls
    data.cols = int(data.height/100*3) #18 with height of 600 pxls
    data.board = []
    for row in range(data.rows):
        data.board += [[0]*data.cols]
    data.snake = [(data.rows//2,data.cols//2)] #start in middle [row][col]
    data.snakeHead = data.snake[0]
    data.cellSize = data.width/data.rows
    data.gameOver = False
    data.moving = False #not moving to start
    data.direction = 'left' #arbitrary assignemnt
    data.timer = 0
    data.newFruit = True
    data.fruitRow = 0 #temp assignments
    data.fruitCol = 0
    data.snakeLength = 1 #units in the snake

def mousePressed(event, data):
    #mouse not used in snake game
    pass

def keyPressed(event, data):
    if (data.gameOver):
        pass
    elif (event.keysym == "Left"): #for each direction, start moving and move in direction
        data.direction = 'left'
        data.moving = True
    elif (event.keysym == "Right"):
        data.direction = 'right'
        data.moving = True
    elif (event.keysym == "Down"):
        data.direction = 'down'
        data.moving = True
    elif (event.keysym == "Up"):
        data.direction = 'up'
        data.moving = True

def timerFired(data):
    if not (data.moving):
        pass
    elif (data.gameOver):
        pass
    else:
        gameOver(data)
        data.timer += 1
        if (data.timer%3 == 0): #move snake every 300 ms
            moveSnake(data)

def moveSnake(data):
    if (data.direction == 'left'):
        newPosition = (data.snakeHead[0],data.snakeHead[1]-1) #move column 1 cell left
    elif (data.direction == 'right'):
        newPosition = (data.snakeHead[0],data.snakeHead[1]+1) #move column 1 cell right
    elif (data.direction == 'down'):
        newPosition = (data.snakeHead[0]+1,data.snakeHead[1]) #move row 1 cell down
    elif (data.direction == 'up'):
        newPosition = (data.snakeHead[0]-1,data.snakeHead[1]) #move row 1 cell up
    data.snake.insert(0,newPosition)
    data.snakeHead = data.snake[0]
    eatFruit(data)
    if not (data.newFruit):
        data.snake.pop() #if a Fruit is not eaten, then remove the last entry in snake

def drawSnake(canvas,data):
    for entry in data.snake:
        x1 = data.cellSize * entry[1] #cell size times col
        y1 = data.cellSize * entry[0] #cel size times row
        x2 = x1 + data.cellSize
        y2 = y1 + data.cellSize
        canvas.create_oval(x1,y1,x2,y2,fill='black')


def eatFruit(data):
    if (data.snakeHead[0] == data.fruitRow) and (data.snakeHead[1] == data.fruitCol):
        data.board[data.fruitRow][data.fruitCol] = 0
        data.newFruit = True

def drawBoard(canvas,data):
    placeFruit(canvas,data)
    data.newFruit = False
    for row in  range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == 1:
                x1 = row*data.cellSize
                x2 = x1 + data.cellSize
                y1 = col*data.cellSize
                y2 = y1 + data.cellSize
                canvas.create_oval(x1,y1,x2,y2,fill='red')

def gameOver(data):
    if (data.snakeHead[1] < 0):
        data.moving = False
        data.gameOver = True
    elif (data.snakeHead[1] > data.cols):
        data.moving = False
        data.gameOver = True
    elif (data.snakeHead[0] < 0):
        data.moving = False
        data.gameOver = True
    elif (data.snakeHead[0] > data.rows):
        data.moving = False
        data.gameOver = True

def placeFruit(canvas,data):
    if (data.newFruit):
        row = random.randint(0,data.rows-1)
        col = random.randint(0,data.cols-1)
        data.board[row][col] = 1
        data.fruitRow = row
        data.fruitCol = col

def drawGameOver(canvas,data):
    canvas.create_text(data.width/2,data.height/2,text='GAME OVER',fill = 'red',font = 'Arial 34 bold')

def redrawAll(canvas, data):
    drawBoard(canvas,data)
    drawSnake(canvas,data)
    if (data.gameOver):
        drawGameOver(canvas,data)

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

run(400, 600)

###############
#test functions
###############

