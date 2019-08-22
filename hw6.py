#Hw6
#Poppa K

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.welcomeMsgSize = 12 #initial size of expanding welcome msg
    data.activeScreen = 'welcome' #initial screen is welcome screen
    data.helpMsgLocation = data.width/2 #start in middle of screen
    data.helpMsgDirection = -1 #move to left initially
    data.callerScreen = data.activeScreen

def mousePressed(event, data):
    if (data.activeScreen == 'help'):
        data.activeScreen = data.callerScreen


def keyPressed(event, data):
    if (event.keysym == "h"):
        data.callerScreen = data.activeScreen
        data.activeScreen = 'help'
    if (event.keysym == "p"):
        data.callerScreen = data.activeScreen
        data.activeScreen = 'game'

def timerFired(data):
    if (data.activeScreen == 'welcome'):
        growWelcomeMessage(data,4)
    elif (data.activeScreen == 'help'):
        moveHelpMessage(data,5)

def moveHelpMessage(data,dLocation):
    if (data.helpMsgDirection == -1): #moving to left
        if (data.helpMsgLocation > data.width*0.25):
            #continue to move left if not at .25*width
            data.helpMsgLocation -= dLocation
        else: #else move right and switch direction to right
            data.helpMsgLocation += dLocation
            data.helpMsgDirection = 1
    else:
        if (data.helpMsgLocation < data.width*0.75):
            #continue to move right if not at .75*width
            data.helpMsgLocation += dLocation
        else: #else move right and switch direction to right
            data.helpMsgLocation -= dLocation
            data.helpMsgDirection = -1

def growWelcomeMessage(data,dFont): #dFont is delta font size
    if (data.welcomeMsgSize < 80):
        data.welcomeMsgSize += dFont
    else:
        data.welcomeMsgSize = 16

def drawHelpScreen(canvas,data):
    helpMsg = "This is not very helpful!"
    helpInstructions = 'Press mouse to return to caller\'s mode'
    canvas.create_text(data.helpMsgLocation,data.height/2,text=helpMsg,font='Arial 30 underline')
    canvas.create_text(data.width/2,data.height/1.25,text=helpInstructions,font = 'Arial 20')

def drawWelcomeScreen(canvas,data):
    welcomeMsg = 'The Hw6 Game-Like App!'
    welcomeMsgFont = 'Arial ' + str(data.welcomeMsgSize)
    welcomeInstructions = 'Press \'p\' to play, \'h\' for help!'
    canvas.create_text(data.width/2,data.height/1.25,text=welcomeInstructions,font='Arial 26')
    canvas.create_text(data.width/2,data.height/2,text=welcomeMsg,font=welcomeMsgFont)

def drawCursor(canvas,data):
    r = 5 #radius of cursor
    xC = data.width/2 #center of x-coor
    yC = data.height/2 #center y-coordinate
    #canvas.create_rectangle(x1,y1,x2,y2,fill='yellow') #placeholder for highlighting active cell
    canvas,create_oval(xC-r,yC-r,xC+r,yC+r,fill="green")

def drawGameScreen(canvas,data):
    drawCursor(canvas,data)

def drawGame(canvas,data):
    if (data.activeScreen == 'welcome'):
        drawWelcomeScreen(canvas,data)
    elif (data.activeScreen == 'help'):
        drawHelpScreen(canvas,data)
    elif (data.activeScreen == 'game'):
        drawGameScreen(canvas,data)

def redrawAll(canvas, data):
    drawGame(canvas,data)

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

def runGameLikeApp():
    rows = 10
    cols = 10
    run(500,500)

runGameLikeApp()