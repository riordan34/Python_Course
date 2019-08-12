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



#################################################
# testAll and main
#################################################
def testAll():
    testIsLatinSquare()

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