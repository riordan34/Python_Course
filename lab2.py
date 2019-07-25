#################################################
# Lab2
#################################################

import cs112_s17_linter
import math

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

def rotate(n):
    len_n = math.ceil(math.log(n,10))
    last = n%10
    n = n//10 + last*10**(len_n-1)
    return n

def isRotation(x, y):
    if x == y:
        return True
    lenx = math.ceil(math.log(x,10))
    tries = 0
    while (tries <= lenx):
        x = rotate(x)
        if x == y:
            return True
        tries += 1
    return False
    
def reverse(n):
    reverse = n%10
    while (n >= 10):
        digit = n//10%10
        reverse = reverse*10 + digit
        n = n//10
    return reverse

def nthEmirpsPrime(n):
    found = 0
    guess = 1
    while (found < n+1):
        guess += 1
        guess2 = reverse(guess)
        if IsPrime(guess):
            if IsPrime(guess2):
                if guess2 != guess:
                    found += 1
    return guess

def carrylessAdd(x1, x2):
    if x2 > x1:
        temp = x1
        x1 = x2
        x2 = temp
    k = 0
    sum = 0
    while (x1 > 0):
        x1_digit = x1%10
        x2_digit = x2%10
        add = x1_digit + x2_digit
        add = (add%10)*10**k
        sum += add
        k += 1
        x1 = x1//10
        x2 = x2//10
    return sum

def isProperty309(n):
    n = abs(n)**5
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    while (n > 0):
        digit = n%10
        if digit == 0:
            zero += 1
        elif digit == 1:
            one += 1
        elif digit == 2:
            two += 1
        elif digit == 3:
            three += 1
        elif digit == 4:
            four += 1
        elif digit == 5:
            five += 1
        elif digit == 6:
            six += 1
        elif digit == 7:
            seven += 1
        elif digit == 8:
            eight += 1
        elif digit == 9:
            nine += 1
        n = n//10
    status = True
    if zero == 0:
        status = False
    if one == 0:
        status = False
    if two == 0:
       status = False
    if three == 0:
        status = False
    if four == 0:
        status = False
    if five == 0:
        status = False
    if six == 0:
        status = False
    if seven == 0:
        status = False
    if eight == 0:
       status = False
    if nine == 0:
        status = False
    return status


def nthWithProperty309(n):
    found = 0
    guess = roundHalfUp(123456789**.2)
    while (found < n+1):
        guess += 1
        if isProperty309(guess):
            found += 1
    return guess
    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed.')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(5) == 635)
    assert(nthWithProperty309(6) == 662)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsRotation()
    testNthEmirpsPrime()
    testCarrylessAdd()
    testNthWithProperty309()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
