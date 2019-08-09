#################################################
# Hw4
#################################################

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
# Problems
#################################################

def highScore(s):
    return s[-1]

def scoreSort(scores):
    #take list of tupples (word, score) and sort high to low
    scores = sorted(scores,key=highScore,reverse=True)
    return scores

def bestScrabbleScore(dictionary, letterScores, hand):
    i = 0
    scores = []
    while (i <  len(dictionary)): #iterate through possible words
        word = dictionary[i]
        handCheck = copy.copy(hand)
        status = True
        score = 0
        for letter in word: #check each letter against letters in hand
            if letter in handCheck: #if letter appears in hand
                #add letterScore to current score
                scoreIndex = string.ascii_lowercase.find(letter)
                score += letterScores[scoreIndex]
                #remove letter from word (can't use it twice)
                handCheck.remove(letter)
            else: #if letter not in hand, then break the loop and move to next word
                status = False
                break
        if (status): #if all letters in dictionary word appear in hand
            pair = (word,score)
            scores.append(pair) #add to list of scores
        i += 1
    for result in scores:
        return result

    '''while (i < len(hand)):
        if hand[i] in dictionary:
            scoreIndex = string.ascii_lowercase.find(hand[i])
            pair = (hand[i],letterScores[scoreIndex])
            scores.append(pair)
        i+=1
    scores = sorted(scores,key=highScore)
    for entry in scores:
        return entry'''
###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def printTortoiseProgram(canvas,program):
    commands = program.split('\n') #split the program by new line
    yText = 10 #initial line
    for command in commands: #read lines one at a time
        canvas.create_text(10,yText,text=command,fill='gray',font='Arial 10',anchor=W)
        yText += 15 #drop 15 pixels for new line

def actionWord(s):
    #get the first word in a string with spaces
    word = ''
    for char in s:
        if not char.isspace(): #if it's not a space, append to output word
            word += char
        else:
            break #end loop if it is space
    return word

def quantityWord(s):
    word =''
    action = actionWord(s)
    i= len(action)+1 #index, start after action word AND space
    while (i < len(s)): #only go for length of string
        if not s[i].isspace():
            word += s[i] #append character to word if not space
            i += 1
        else:
            break
    return word

def drawAction(canvas,color,position,distance,angle):
    xC = position[0] #starting x-coordinate
    yC = position [1] #starting y-coordinate
    newXC = xC + distance*math.cos(angle) #end x-coord
    newYC = yC - distance*math.sin(angle) #end y-coord
    if color != 'none': #only draw if color is not none
        canvas.create_line(xC,yC,newXC,newYC,fill=color,width=4)
    return (newXC,newYC) #return new X and Y regardless

def tortoiseAction(canvas, command, color, position, angle):
    distance = 0 #in case only color changes
    action = actionWord(command)
    quantity = quantityWord(command)
    if action == 'color': #if command is color
        color = quantity #set new color
    elif action == 'left': #if command is left
        angle += (math.pi/180)*int(quantity) #move radians counterclockwise
    elif action == 'right':
        angle -= (math.pi/180)*int(quantity) #move radians clockwise
    elif action == 'move': #if command is move, set distance of total move
        distance = int(quantity)
    position = drawAction(canvas,color,position,distance,angle)
    return (position,angle,color)

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    color = 'red' #arbitrary initial color
    position = (winWidth/2,winHeight/2) #start in middle of screen
    angle = 0 #start moving directly right
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    printTortoiseProgram(canvas, program)
    commands = program.split('\n') #split the program by new line
    for command in commands: #read lines one at a time
        if actionWord(command) == '#':
            continue #go to next line if line starts as comment
        elif actionWord(command) == '': #skip if line is blank
            continue
        else:
            (position,angle,color) = tortoiseAction(canvas,command,color,position,angle)

    root.mainloop()

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testRunSimpleTortoiseProgram()
    #testBestScrabbleScore()
    #testRunSimpleProgram()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,del,is,pass,repr' +
        'as,class,except,finally,global,lambda,nonlocal,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len,'+
        #'ascii,bin,dir,enumerate,format,help,hex,id,iter,'+
        #'list,oct,slice,sorted,tuple,zip,'+
        '__import__,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,' +
        'eval,exec,filter,frozenset,getattr,globals,' +
        'hasattr,hash,issubclass,' +
        'locals,map,memoryview,next,object,open,property,set,' +
        'setattr,staticmethod,super,' +
        'type,vars,importlib,imp,{,}')
    #cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
