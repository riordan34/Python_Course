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

def largestColumn(a):
    #find the largest column in case of ragged 2D list
    rows = len(a)
    cols = 0
    for row in range(rows):
        col = len(a[row])
        if col > cols:
            cols = col
    return cols

def removeRowAndCol(A,row,col):
    deleteRow = row
    deleteCol = col
    B = [] #blank list to append values
    rows = len(A)
    cols = largestColumn(A) #get length of longest column
    for row in range(rows):
        newRow = []
        if row == deleteRow: #don't append if it is the row to remove
            continue
        else:
            for col in range(cols):
                if col == deleteCol: #don't append if it is column to remove
                    continue
                else:
                    newRow += [A[row][col]] #create new row
        B += [newRow] #add row to 2D list
    return B

def destructiveRemoveRowAndCol(A,row,col):
    deleteRow = A[row]
    A.remove(deleteRow) #remove entire row first
    rows = len(A)
    for row in range(rows):
        #in each row, delete the index of column
        del A[row][col]
    return None

def isPerfectSquare(n):
    root = math.sqrt(n)
    intRoot = int(root)
    if root**2 == intRoot**2:
        return True
    else: return False

def areLegalValues(values):
    N = len(values)
    if not isPerfectSquare(N):
        return False #check to see if length is perfect square
    if max(values) > N or min(values) < 0:
        return False #check to see if numbers between 0 and N
    for number in range(1,N+1): #check each number 1 to N
        count = 0
        for value in range(N): #check each index
            if values[value] == number:
                count += 1 #add to count if number appears
        if count > 1: #if it appears more than once
            return False #return false and break
            break
    return True

def isLegalRow(board,row):
    rowCheck = board[row]
    return areLegalValues(rowCheck)

def isLegalCol(board,col):
    colList = [board[i][col] for i in range(len(board))]
    return areLegalValues(colList)

def isLegalBlock(board,block):
    blockList = []
    N = len(board)
    step = int(math.sqrt(N)) #each block contains sqrt(N) rows and cols
    for i in range(0,N,step): #check every sqrt(N) rows
        if block >= i and block < i + step: #if block is in range
            rows = range(i,i+step) #assign it to rows
    for j in range(0,step): #check values from 0 to sqrt(N)
        if block%step == j: #remainder of block/sqrt(N) gives column group
            start = j*step #start of column range is column group times number of groups
            cols = range(start,start+step) #column range = start + step
    for row in rows:
        for col in cols: #go through applicable rows and cols and add to list
            blockList += [board[row][col]]
    return areLegalValues(blockList)

def isLegalSudoku(board):
    rows = cols = blocks = len(board)
    for row in range(rows):
        if not isLegalRow(board,row):
            return False
            break
    for cols in range(cols):
        if not isLegalCol(board,cols):
            return False
            break
    for block in range(blocks):
        if not isLegalBlock(board,block):
            return False
            break
    return True



#################################################
# Test Functions

def testRemoveRowAndCol():
    print("Testing removeRowAndCol()...", end="")
    assert(removeRowAndCol([[2, 3, 4, 5],[8, 7, 6, 5],[0, 1, 2, 3]],1,2) == [[2, 3, 5], [0, 1, 3]])
    assert(removeRowAndCol([[5,3,8,4],[3,8,4,5],[8,4,5,3],[4,5,3,8]],0,3) == [[3,8,4],[8,4,5],[4,5,3]])
    assert(removeRowAndCol([[5,3,8,4],[3,8,6,5],[8,4,5,3],[4,5,3,8]],3,0) == [[3,8,4],[8,6,5],[4,5,3]])
    print("Passed!")

def testIsLegalSudoku():
    board1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    board2 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 5, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 0, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    board3 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [5, 0, 0, 0, 8, 0, 0, 7, 9]]
    board4 = [[1,2,3,4], [3,4,1,2], [2,3,4,1], [4,1,2,3]]
    print("Testing isLegalSudoku()...",end='')
    assert(isLegalSudoku(board1) == True)
    assert(isLegalSudoku(board2) == False)
    assert(isLegalSudoku(board3) == False)
    assert(isLegalSudoku(board4) == True)
    print("Passed!")

#################################################
# testAll and main
#################################################
def testAll():
    testRemoveRowAndCol()
    testIsLegalSudoku()

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