#################################################
# Hw2
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

def isKaprekar(n):
    if n <= 0:
        return False
    k = n**2
    if k < 10:
        if k == n:
            return True
    tries = math.ceil(math.log(k,10))
    count = 1
    while (count < tries):
        k_back = k%10**count
        k_front = k//10**count
        if k_back == 0:
            count += 1
            continue
        if k_back + k_front == n:
            return True
            break
        count += 1
    return False

def nthKaprekarNumber(n):
    found = 0
    guess = 0
    while (found < n+1):
        guess += 1
        if isKaprekar(guess):
            found += 1
    return guess

def trapArea(a,b,h):
    area = (a+b)*(h/2)
    return area

def integral(f, a, b, N):
    integral = 0
    h = (b-a)/N
    count = 0
    x1 = a
    x2 = a + h
    while (count < N):
       y1 = f(x1)
       y2 = f(x2)
       area = trapArea(y1,y2,h)
       integral += area
       x1 = x2
       x2 += h
       count += 1
    return integral

def nearestKaprekarNumber(n):
    delta_down = n - math.floor(n)
    delta_up = math.ceil(n)-n
    if isKaprekar(n):
        return n
    n_down = n - delta_down
    n_up = n + delta_up
    while (True):
        if isKaprekar(n_down):
            if isKaprekar(n_up):
                if abs(n_up - n) < abs(n_down - n):
                    return n_up
                    break
                else:
                    return n_down
                    break
            else:
                return n_down
                break
        if isKaprekar(n_up):
            return n_up
            break
        n_up += 1
        n_down -= 1

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

def carrylessMultiply(x1, x2):
    product = 0
    if x2 > x1:
        temp = x1
        x1 = x2
        x2 = temp
    i = 0
    hold = x1
    while (x2>0):
        x1 = hold
        x2_digit = x2%10
        k = 0
        sum = 0
        while (x1>0):
            x1_digit = x1%10
            sum += ((x1_digit*x2_digit)%10)*10**k
            x1 = x1//10
            k += 1
        x2 = x2//10
        product = carrylessAdd(product,sum*10**i)
        i += 1
    return product

def digitSum(n):
    digit_sum = 0
    while(n>0):
        digit = n%10
        digit_sum += digit
        n = n//10
    return digit_sum
    
def primeFactorSum(n):
    sum = 0
    while (not IsPrime(n)):
        maxFactor = roundHalfUp(n**0.5)
        for factor in range(2,maxFactor+1):
            if (n % factor == 0):
                if IsPrime(factor):
                    sum += digitSum(factor)
                    factor_pair = n//factor
                    if IsPrime(factor_pair):
                        sum += digitSum(factor_pair)
                        n = factor_pair
                        break
                    else:
                        n = factor_pair
    return sum
    

def isSmithNumber(n):
    status = False
    digits = digitSum(n)
    factors = primeFactorSum(n)
    if digits == factors:
        status = True
    return status


def nthSmithNumber(n):
    found = 0
    guess = 1
    while (found < n +1):
        guess += 1
        if isSmithNumber(guess):
            found += 1
    return guess

##### Bonus #####

def play112(game):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testNthKaprekarNumber()
    testIntegral()
    testNearestKaprekarNumber()
    testCarrylessMultiply()
    testNthSmithNumber()
    #testBonusPlay112()

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
        #'range,reversed,str,' # added 'str' for play112 bonus
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
