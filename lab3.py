#################################################
# Lab3
#################################################

#import cs112_s17_linter
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
# Exercises
#################################################

def longestCommonSubstring(s1, s2):
    if len(s2) > len(s1):
        temp = s1 #keep s1 longest string
        s1 = s2
        s2 = temp
    lenCommon = 0 #length of common substring
    common =''
    i = 0 #s2 index
    k = 1 #additional search index, move k characters from i each time
    while (i < len(s2)):
        if s2[i:i+k] in s1: #if substring in longer string
            if k > len(common): #make longest string if longest
                common = s2[i:i+k]
            if k ==  len(common): #make longest string if equal but smaller lexi..
               if s2[i:i+k] < common:
                   common = s2[i:i+k]
            k += 1
        else: #reset k, move to next start position in s2
            k = 1
            i += 1
    return common

def reverseString(s):
    return s[::-1]

def encodeRightLeftCipher(text, rows):
    encoded = str(rows) #start of encoded string with rows
    emptySpaces = rows - len(text)%rows #spaces that need to be populated by lowercase
    i = 0
    while (i < emptySpaces):
        i += 1
        #add from end of lowercases, move left, wrap if need be
        text += string.ascii_lowercase[(-i%26)]
    row = 0
    while (row < rows): #go row by row
        char = 0
        substring = '' #temporary string, use for potential reversal
        while (char < len(text)):
            if char%rows == row:
                substring += text[char] #add to substring if it belongs in current row
            char += 1
        if row%2 != 0: #if it is an odd row, reverse it before adding to encoded
            substring = reverseString(substring)
        encoded += substring
        row += 1
    return encoded

def decoderReorder(cipher):
    #undo reversal of strings
    decoded =''
    rows = int(cipher[0]) #pull out number of rows
    cipher = cipher [1:]
    row = 0
    columns = math.ceil(len(cipher)/rows)
    while (row < rows):
        char = 0 + row * columns #starting char in each row
        substring =''
        while (char < (row + 1) * columns):
            substring += cipher[char]
            char += 1
        if row%2 != 0: #reverse if odd
            substring = reverseString(substring)
        decoded += substring #append to partially decoded string
        row += 1
    decoded = str(rows) + decoded #add back in the number of rows for full decoding
    return decoded

def decodeRightLeftCipher(cipher):
    decoded =''
    cipher = decoderReorder(cipher) #return single string with no row reversal
    rows = int(cipher[0]) #number of rows
    cipher = cipher[1:]
    column = 0
    columns = math.ceil(len(cipher)/rows) #number of columns
    while (column < columns):
        char = 0
        substring =''
        while (char < len(cipher)):
            if char%columns == column:
                #add to substring if it belongs in current column and is uppercase
                if cipher[char].isupper():
                    substring += cipher[char]
            char += 1
        decoded += substring
        column += 1
    return decoded


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testEncodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 4
    # W T A W
    # E A T N
    # A C D z
    # T K A y
    rightLeft = "4"+"WTAWNTAEACDzyAKT"
    cipher = encodeRightLeftCipher(text, rows)
    assert(rightLeft == cipher)
    print("passed!")

def testDecodeRightLeftCipher():
    print("testing decodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 6
    cipher = encodeRightLeftCipher(text, rows)
    plaintext = decodeRightLeftCipher(cipher)
    assert(plaintext == text)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testEncodeRightLeftCipher()
    testDecodeRightLeftCipher()

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
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    #cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
