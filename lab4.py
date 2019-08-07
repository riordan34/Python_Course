#################################################
# Lab4
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

def lookAndSay(a):
    tuple = []
    if len(a) == 0:
        return tuple #return blank if initial blank
    count = 1 #set count to 1, everything appears at least once
    value = 0
    for entry in range(len(a)-1):
        value = a[entry] #if number is consecutive, add to count
        if a[entry] == a[entry+1]:
            count +=1
        else:
            pair = (count,value) #create count/value pair
            tuple.append(pair) #append it to output list
            count = 1 #reset count
    value = a[-1] #account for last entry if it is different from prior
    pair = (count,value)
    tuple.append(pair)
    return tuple


def inverseLookAndSay(a):
    list =[]
    v = 1 #value index
    c = 0 #count index
    for entry in a:
        count = entry[c]
        i = 0
        while (i < count): #append value as many times as count
            list.append(entry[v])
            i += 1
    return list


def stringToDigits(s,decode):
    digitString = ''
    for item in s: #go through each letter in string
        if not item.isalpha():
            digitString += item #add to string if not a letter
        else:
            for pair in decode: #check against decoder
                #if letter appears in index 1 of decoder tupple
                if item == pair[1]:
                    digitString += str(pair[0]) #replace w/ digit
    return digitString


def solutionDecoder(s):
    #create tupple of character and corresponding digit
    letterDigit = []
    i = 0
    while (i < len(s)):
        if s[i].isalpha: #if it is a letter
            pair = (i,s[i]) #create tupple of letter and digit pair
            letterDigit.append(pair) #add it to the list
        i += 1
    return letterDigit

def findTerms(s):
    #find operators,operand and solution in string
    equal = s.find('=') #equal sign index
    add = s.find('+') #plus sign index
    op1 = s[:add] #operand 1
    op2 = s[add+1:equal] #operand 2
    solution = s[equal+1:] #solution
    return (op1,op2,solution) #return list

def solvesCryptarithm(puzzle, solution):
    for item in puzzle:
        #return false if letter in puzzle not in proposed solution
        if item.isalpha() and item not in solution:
            return False
            break
    decoder = solutionDecoder(solution) #get decoder pairs
    digitString = stringToDigits(puzzle,decoder) #return digitString
    partsList = findTerms(digitString) #get parts
    return int(partsList[0]) + int(partsList[1]) == int(partsList[2])


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def getData(s):
    results = []
    vowels = 'aeiouAEIOU' #vowel string
    v = 0 #vowel variable
    c = 0 #consonent variable
    other = 0
    for char in s:
        if char in vowels:
            v += 1 #add if in vowel string
        elif char.isalpha():
            c += 1 #add if alpha not in vowel string
        elif not char.isspace():
            other += 1 #add if not space
    total = v + c + other
    if total == 0:
        return False #return false if no data
    else:
        vPercent = roundHalfUp(v/total*100)
        cPercent = roundHalfUp(c/total*100)
        otherPercent = roundHalfUp(other/total*100)
        return (v,vPercent,c,cPercent,other,otherPercent,total)

def drawVowelArc(canvas,box,start,extent):
        canvas.create_arc(box, start=start, extent=extent, fill="pink")

def makeLetterTypePieChart(text, winWidth=500, winHeight=500):
    params = getData(text)
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    if params == False: #if no data, return no data
        canvas.create_text(winWidth/2, winHeight/2,
                       text="No data to display", font="Arial 20 bold")
    minDim = min(winWidth,winHeight) #find min dimension
    boxParams=(0.05*minDim,0.05*minDim,0.95*minDim, 0.95*minDim)
    #params structure = (vowels, %, consonents, %, other, %, total)
    if params[0] != 0:   #if there are vowels
        vText = 'vowels (%d of %d, %d' %(params[0],params[6],params[1])+'%)'
        if params[1] == 100: #create circle if 100%
            canvas.create_oval(boxParams, fill='pink')
        else:
            vArcLength = params[1]/100*360 #arc Length
            drawVowelArc(canvas,boxParams,90,vArcLength)
    if params[2] != 0:   #if there are consonents
        start = 90 + vArcLength
        cArcLength = params[3]/100*360
        canvas.create_arc(boxParams, start=start, extent=cArcLength, fill="cyan")
    if params[4] != 0:   #if there are others
        start = 90 + vArcLength + cArcLength
        arcLength = params[5]/100*360
        canvas.create_arc(boxParams, start=start, extent=arcLength, fill="lightGreen")
    root.mainloop()


def testMakeLetterTypePieChart():
    print("Testing makeLetterTypePieChart()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    makeLetterTypePieChart("AB, c de!?!")
    makeLetterTypePieChart("AB e")
    makeLetterTypePieChart("A")
    makeLetterTypePieChart("               ")
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testMakeLetterTypePieChart()

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
