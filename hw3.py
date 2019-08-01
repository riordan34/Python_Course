#################################################
# Hw3
#################################################

import cs112_s17_linter
import math, string

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

def patternedMessage(msg, pattern):
    pattern = pattern.strip()
    patternedMessage = ''
    spacelessMsg = ''
    #get msg without spaces
    for char in msg:
        if not char.isspace():
            spacelessMsg += char
    i = 0 #pattern Index
    k = 0 #msg Index
    while (i < len(pattern)):
        if pattern[i] ==  ' ':
            patternedMessage += " "
        elif pattern[i] == '\n':
            patternedMessage +='\n'
        else:
            patternedMessage += spacelessMsg[k%len(spacelessMsg)] #allow it to loop around
            k +=1 #go to next msg index
        i += 1
    return patternedMessage


def bestStudentAndAvg(gradebook):
    highStudent = ''
    highAvg = -1000
    for line in gradebook.splitlines():
        if len (line) == 0 or line[0] == '#':
            continue #ignore lines that aren't names/numbers
        else:
            currentStudent = '' #get name of current student
            currentTotal = 0 #for summing all grades
            entries = 0 #keep track of inputs for averaging
            for entry in line.split(','):
                if entry.isalpha():
                    currentStudent = entry #record current Student
                else:
                    currentTotal += int(entry)
                    entries += 1
            avgScore = currentTotal/entries #calculate Average
            if avgScore > highAvg: #if it's the highest
                highAvg = roundHalfUp(avgScore) #make high score
                highStudent = currentStudent #record students name
    return ('%s:%d' % (highStudent, highAvg))

###### BONUS #######

#def topLevelFunctionNames(code):

### Get Eval Functions ###
def getPreOperand(expr,i):
    pre = i - 1 #look backwards to see where operand1 starts
    while (pre > 0 and expr[pre-1] in string.digits):
        pre -= 1 #look at preceding index if it is number
    return pre

def getPostOperand(expr,i,operator):
    post = i + len(operator) #look foward, starting after operator
    while (post < len(expr) and expr[post] in string.digits):
        post += 1
    return post

def nextAddSubtractIndex(expr):
    i = 0
    index = -1 #set to negative 1 initially
    while (i < len(expr)):
        if expr[i] == '+' or expr[i] == '-':
            index = i #find first occurence and and set that as index
            break
        i += 1
    return index #return index, or negative one if it doesn't exist

def nextMultDivideIndex(expr):
    i = 0
    index = -1 #set to negative 1 initially
    while (i < len(expr)):
        if expr[i] == '*' or expr[i] == '/' or expr[i] == '%':
            index = i #find first occurence and and set that as index
            break
        i += 1
    return index #return index, or negative one if it doesn't exist

def evalMultDivide(expr):
    i = getMultDivideIndex(expr)
    result = 0
    operator = expr[i]
    if expr[i+1] == '/':#if next index is slash, then int division
        operator = '//'
    pre = getPreOperand(expr,i) #get operand before and after operator
    post = getPostOperand(expr,i,operator)
    op1 = int(expr[pre:i])
    op2 = int(expr[i+len(operator):post])
    if (operator == '//'): #go through possibilities of operators
        result = op1//op2
    elif (operator == '/'):
        result = op1/op2
    elif (operator == '*'):
        result = op1*op2
    else:
        result = op1%op2
    expr = expr[:pre]+str(result)+expr[post:]
    return expr

def evalAddSubtract(expr):
    i = nextAddSubtractIndex(expr) #same concept as mult divide
    result = 0
    pre = getPreOperand(expr,i)
    post = getPostOperand(expr,i,"+")
    op1 = int(expr[pre:i])
    op2 = int(expr[i+1:post])
    if (expr[i] == '+'):
        result = op1+op2
    else:
        result = op1-op2
    expr = expr[:pre]+str(result)+expr[post:]
    return expr

def evalExponents(expr,i):
    result = 0 #same concept as mult divide
    pre = getPreOperand(expr,i)
    post = getPostOperand(expr,i,"**")
    op1 = int(expr[pre:i])
    op2 = int(expr[i+2:post])
    result = op1**op2
    expr = expr[:pre]+str(result)+expr[post:]
    return expr


def getEvalSteps(expr):
    steps = 0
    leadIndent = len(expr)*' '+' = '
    evalExpr = expr + ' = '
    while (expr.find("**") > 0):
        expr = evalExponents(expr,expr.find('**'))
        if steps == 0:
            evalExpr += expr
        else:
            evalExpr +='\n'+leadIndent+expr
        steps += 1
    while (nextMultDivideIndex(expr) > 0):
        expr = evalMultDivide(expr)
        if steps == 0:
            evalExpr += expr
        else:
            evalExpr +='\n'+leadIndent+expr
        steps += 1
    while (nextAddSubtractIndex(expr) > 0):
        expr = evalAddSubtract(expr)
        if steps == 0:
            evalExpr += expr
        else:
            evalExpr +='\n'+leadIndent+expr
        steps += 1
    if steps == 0:
        evalExpr += expr
    return evalExpr


######### Bonus Encode/Decode section ######
def bonusEncode1(msg):
    result = ''
    for c in msg:
        if (c.islower()):
            c = chr(ord('a') + (ord(c) - ord('a') + 1)%26)
        result += c
    return result

def bonusDecode1(msg):
    ans = ''
    for char in msg:
        if char in string.ascii_lowercase:
            i = string.ascii_lowercase.find(char)
            ans += string.ascii_letters[i-1]
        else: ans += char
    return ans

def bonusEncode2(msg):
    result = ""
    p = string.ascii_letters + string.digits
    for i in range(len(msg)):
        c = msg[i]
        if (c in p): c = p[(p.find(c) - i) % len(p)]
        result += c
    return result

def bonusDecode2(msg):
    result = ""
    p = string.ascii_letters + string.digits
    for i in range(len(msg)):
        c = msg[i]
        if (c in p): c = p[(p.find(c) + i) % len(p)]
        result += c
    return result

def bonusEncode3(msg):
    result = ""
    prev = 0
    for i in range(len(msg)):
        curr = ord(msg[i])
        if (result != ""): result += ","
        if ((i+1) % 15 == 0): result += "\n"
        result += str(curr - prev)
        prev = curr
    return result

def bonusDecode3(msg):
    msg=msg.split(',')
    result = chr(int(msg[0]))
    i = 1
    previous = int(msg[0])
    while (i < len(msg)):
        next = previous + int(msg[i])
        result += chr(next)
        previous = next
        i += 1
    return result

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################




#################################################
# playPig (be sure this is below the # ignore_rest line!
#################################################
import random

def turnSequence(score,winning):
    needed = winning - score #necessary remaining points to win
    turnTotal = 0
    while (True):
        decision = input ('\nWould you like to Roll or Hold?\n')
        if decision.lower() == 'hold':
            break #end turn if hold is selected
        if decision.lower() == 'roll':
            roll = random.randint(1,6)
            #end turn and reset turn total to 0 if 1 is rolled
            if roll == 1:
                turnTotal = 0
                #return roll results
                print ('\nSorry, you rolled a %d\n' %roll)
                break
            else:
                turnTotal += roll
                #return roll results
                print ('\nYou rolled a %d. Your turn total is: %d\n' %(roll, turnTotal))
                if turnTotal >= needed:
                    break
    return turnTotal



def playPig():
    print("Welcome to Pig\n")
    winningScore = int(input ('What score would you like to play to?\n'))
    #initial scores are 0
    player1Score = player2Score = 0
    turn = 0
    winner = ''
    while (True):
        #print socre
        print ('\nPlayer 1: %d -- Player 2: %d\n' % (player1Score, player2Score))
        #if 'turn' is even, player 1 turn, else player 2
        if turn%2 == 0:
            print ('It is player 1\'s turn')
            #run turn sequence
            outcome = turnSequence(player1Score,winningScore)
            player1Score += outcome #add turn sequence to total
            #if new total is above limit, end game
            if player1Score >= winningScore:
                winner = 'Player 1'
                break
        else:
            #repeat above for player 2
            print ('It is player 2\'s turn')
            outcome = turnSequence(player2Score,winningScore)
            player2Score += outcome
            if player2Score >= winningScore:
                winner = 'Player 2'
                break
        turn += 1 #go to next turn after sequence if winning score not met
    print ('\nPlayer 1: %d -- Player 2: %d\n' % (player1Score, player2Score))
    print ('Congratulations %s! You are the winner!' %winner)


#################################################
# Test Functions
#################################################

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        msg,pattern = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assert(observed == soln)
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

import random

def testBonusDecode(testFn, encodeFn, decodeFn):
    print("Testing " + testFn + "...", end="")
    s1 = ""
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(" \n\n") + random.choice(string.digits)
    for s in ["a", "abc", s1]:
        assert(decodeFn(encodeFn(s)) == s)
    print("Passed!")

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

def testBonusDecode3():
    testBonusDecode("testBonusDecode3", bonusEncode3, bonusDecode3)

#################################################
# testAll and main
#################################################

def testAll():
    testPatternedMessage()
    testBestStudentAndAvg()
    #testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()
    testBonusDecode1()
    testBonusDecode2()
    testBonusDecode3()

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
