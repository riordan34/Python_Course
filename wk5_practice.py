#Ken Riordan
#week 4 practice
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
# Autograded Exercises
#################################################

def isLatinSquare(a):
    initialChecklist = []
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        currentChecklist = []
        for col in range(cols):
            currentChecklist.append(a[row][col])
        if initialChecklist == []:
            initialChecklist = currentChecklist
        elif initialChecklist != currentChecklist:
            return False
    return True

def isSquareList(a):
    rows = len(a) #number of rows
    for row in range(rows):
        if len(a[row]) != rows: #if number of columns in given row not equal to rows
            return False #its not square, return false and break
            break
    return True #else return true

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



def isKnightsTour(a):
    if (isSquareList(a)): #ensure it's a NxN (square) list
        moves = len(a)**2
        for move in range(1,moves): #check each number from 1 to n^2
            #get initial position
            (startRow,startCol) = findNextLocation(a,move)
            #then get position of next move
            (nextRow,nextCol) = findNextLocation(a,move+1)
            #check if distance equals sqrt(5) (2 in 1 direction, on in other)
            if math.sqrt((startRow-nextRow)**2 + (startCol-nextCol)**2) != math.sqrt(5):
                return False
                break
        return True
    return False

def queenCheckRow(a,row,cols):
    count = 0 #count of queens in row
    for col in range(cols): #check each column in row for a Queen
        if (a[row][col]):
            count += 1
    if count > 1: #should have one and only one queen in row
        return False
    else: return True

def queenCheckCol(a,col,rows):
    count = 0 #count of queens in row
    for row in range(rows): #check each row in column for a Queen
        if (a[row][col]):
            count += 1
    if count > 1:#should have one and only one queen in column
        return False
    else: return True

def queenCheckDiagonal(a,row,col,rows,cols):
    iniRow = row
    iniCol = col #keep track of initial row/column
    #Check up and left
    while (row > 0 and col > 0):
        if (a[row-1][col-1]):
            return False
            break
        else:
            row -= 1
            col -= 1
    #Check up and right
    row = iniRow #reset to initial row/column
    col = iniCol
    while (row > 0 and col < cols-1):
        if (a[row-1][col+1]):
            return False
            break
        else:
            row -= 1
            col += 1
    #Check down and left
    row = iniRow #reset to initial row/column
    col = iniCol
    while (row < rows-1 and col > 0):
        if (a[row+1][col-1]):
            return False
            break
        else:
            row += 1
            col -= 1
    #Check down and right
    row = iniRow #reset to initial row/column
    col = iniCol
    while (row < rows-1 and col < cols-1):
        if (a[row+1][col+1]):
            return False
            break
        else:
            row += 1
            col += 1
    return True

def nQueensChecker(a):
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            if (a[row][col]):
                if not queenCheckRow(a,row,cols):
                    return False
                    break
                elif not queenCheckCol(a,col,rows):
                    return False
                    break
                elif not queenCheckDiagonal(a,row,col,rows,cols):
                    return False
                    break
    return True


#################################################
# Test Functions

def testIsLatinSquare():
    print("Testing isLatinSquare()...", end="")
    assert(isLatinSquare([[1,2],[2,1]]) == True)
    assert(isLatinSquare([[5,3,8,4],[3,8,4,5],[8,4,5,3],[4,5,3,8]]) == True)
    assert(isLatinSquare([[5,3,8,4],[3,8,4,5],[8,4,5,3],[4,5,3,8]]) == True)
    assert(isLatinSquare([[5,3,8,4],[3,8,6,5],[8,4,5,3],[4,5,3,8]]) == False)
    assert(isLatinSquare([[1,2],[2,3]]) == False)
    print("Passed!")

def testIsKnightsTour():
    print("Testing isKnightsTour()...", end="")
    assert(isKnightsTour([[1,2],[3,4]]) == False)
    assert(isKnightsTour([[5,3,8,4],[3,8,4,5],[8,4,5,3],[4,5,3]]) == False)
    assert(isKnightsTour([[3,22,13,16,5],[12,17,4,21,14],[23,2,15,6,9],[18,11,8,25,20],[1,24,19,10,7]]) == True)
    assert(isKnightsTour([[7,12,15,20,5],[16,21,6,25,14],[11,8,13,4,19],[22,17,2,9,24],[1,10,23,18,3]]) == True)
    assert(isKnightsTour([[[1, 4, 7], [6, 9, 2], [3, 8, 5]]]) == False)
    print("Passed!")

def testNQueensChecker():
    print("Testing nQueenChecker()...", end="")
    assert(nQueensChecker([[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]]) == True)
    assert(nQueensChecker([[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,True,False,False]]) == False)
    assert(nQueensChecker([[False,True,False,False,False,False,False,False],[False,False,False,True,False,False,False,False],[False,False,False,False,False,True,False,False],[False,False,False,False,False,False,False,True],[False,False,True,False,False,False,False,False],[True,False,False,False,False,False,False,False],[False,False,False,False,False,False,True,False],[False,False,False,False,True,False,False,False]]) == True)
    print("Passed!")

#################################################
# testAll and main
#################################################
def testAll():
    #testIsLatinSquare()
    testIsKnightsTour()
    testNQueensChecker()

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