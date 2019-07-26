#################################################
# Week3 Practice
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
# Tue Lecture
# Poppa K - 7/25/2019
#################################################

def vowelCount(s):
    s = s.lower()
    vowelCounter = 0
    vowels = "aeiou"
    for vowel in vowels: #check one vowel at a time
        for letter in s: #check each letter against vowel
            if vowel == letter:
                vowelCounter += 1 #add 1 for each vowel found
    return vowelCounter

def interleave(s1, s2):
    newString = ""
    shorter = 0
    longer = 0
    #set length of loop to shorter string
    if len(s1)<len(s2):
        shorter = s1
        longer = s2 #record longer string
    else:
        shorter = s2
        longer = s1
    i = 0
    #loop through strings adding the i-th index each time
    while (i < len(shorter)):
        newString += s1[i] + s2[i]
        i += 1
    #add any leftover letters from the longer string
    newString += longer[len(shorter):]
    return newString

def hasBalancedParentheses(s):
    unmatched = 0
    for char in s: #loop through each character in string
        if char == "(":
            unmatched += 1 #add 1 for left paranthesis
        elif char == ")":
            if unmatched > 0: #subtract if it closes left paranthesis
                unmatched -= 1 #don't allow unmatched to go negative
            elif unmatched == 0:
                return False #end if right paranthesis doesn't have open match
                break
    if unmatched == 0:
        return True
    else:
        return False


#################################################
# Wed Recitation
#################################################

def rotateStringLeft(s, k):
    k = k%len(s) #account for multiple rotations
    new_start = s[k:] #string from k to end
    new_end = s[:k] #string from start to k
    rotatedString = new_start + new_end
    return rotatedString

def rotateStringRight(s, k):
    k = k%len(s) #account for multiple rotations
    new_start = s[-k:] #string from -k to end
    new_end = s[:-k] #string from start to -k
    rotatedString = new_start + new_end
    return rotatedString

def wordWrapSpaces(text,width):
    wrappedString =''
    i = 0
    while (i < len(text)):
        if i > 0 and i%width == 0:
            wrappedString += '\n' + text[i]
        else:
            wrappedString += text[i]
        i += 1
    return wrappedString

def wordWrap(text, width):
    spacelessWrap =''
    wrappedString = wordWrapSpaces(text,width)
    for line in wrappedString.splitlines():
        spacelessWrap += line.strip() + '\n'
    spacelessWrap = spacelessWrap[:-1].replace(" ","*")
    return spacelessWrap


def largestNumber(s):
    large = -1 #arbitrary large
    for words in s.split(" "): #split on whitespace to find 'words
        digit = -1
        if words.isdigit():
            digit = int(words)
            if digit > large: #assign current number if larger than prev.
                large = digit
    if large == -1:
        return None
    else:
        return large

#################################################
# Thu Lecture
#################################################

def reverseString(s):
    return s[::-1]

def isPalindrome1(s):
    return (s == reverseString(s))

def longestSubpalindrome(s):
    i = 0
    longest=""
    while (i < len(s)):
        subIndex = i+1
        current_long = ""
        while (subIndex <= len(s)):
            check = s[i:subIndex]
            if isPalindrome1(check):
                current_long = check
                if len(current_long) == len(longest):
                    if current_long > longest:
                        longest = current_long
                elif len(current_long) > len(longest):
                    longest = current_long
            subIndex += 1
        i += 1
    return longest

def lowerLettersOnly(s):
    letters = ""
    for char in s:
        if char.isalpha():
            letters += char.lower()
    return letters

def leastFrequentLetters(s):
    s = lowerLettersOnly(s) #get only lowercase letters
    lowCount = len(s) #max times a letter can appear
    lowString = '' #blank answer
    lowLetter = '' #temp blank for possible replacement
    for letter in string.ascii_lowercase: #check all lower case alphas
        count = s.count(letter) #apparence of loweralpha in string
        #letter must appear at least once
        if count >=1 and count == lowCount: #append to answer and temp if equal
            lowString += letter
            lowLetter += letter
        elif count >= 1 and count < lowCount: #replace answer and temp if less
            lowString = lowString.replace(lowLetter,letter)
            lowLetter = letter
            lowCount = count
    return lowString


# some interactive console game!

#################################################
# Extra Practice
#################################################

def unique(s):
    uniqueChars = ''#blank string for unique chars only
    for letter in string.ascii_letters: #check upper and lower appearences
        if letter in s:
            uniqueChars += letter #append char if it appears in string
    return uniqueChars


def sameChars(s1, s2):
    if not isinstance(s1,str) and isinstance(s2,str):
        return False #false if one or both not strings
    uniqueS1 = unique(s1)
    uniqueS2 = unique(s2)
    return uniqueS1 == uniqueS2 #check unique strings against each other

def mostFrequentLetters(s):
    s = lowerLettersOnly(s) #get only lowercase letters
    highCount = 0 #initial tally of max
    highString = '' #blank answer
    highLetter = '' #temp blank for possible replacement
    for letter in string.ascii_lowercase: #check all lower case alphas
        count = s.count(letter) #apparence of loweralpha in string
        #letter must appear at least once
        if count >= 1 and count == highCount: #append to answer and temp if equal
            highString += letter
            highLetter += letter
        elif count >= 1 and count > highCount: #replace answer and temp if more
            highString = highString.replace(highLetter,letter)
            highLetter = letter
            highCount = count
    return highString.upper()

def areAnagrams(s1, s2):
    status = True
    s1 = lowerLettersOnly(s1) #get only lowercase letters
    s2 = lowerLettersOnly(s2)
    for letter in string.ascii_lowercase:
        #if count of any letter is not the same, return false and break
        if s1.count(letter) != s2.count(letter):
            status = False
            break
    return status


def collapseWhitespace(s):
    collapsedString = ''
    i = 0 #string index
    while (i < len(s)):
        #add char to new string if not whitespace
        if s[i] not in string.whitespace:
            collapsedString += s[i]
            i += 1
        #add space to end new string if is whitespace
        elif s[i] in string.whitespace and i == len(s)-1:
            collapsedString += " "
            i += 1
        #add space to new string if is whitespace and next char is not whitespace
        elif s[i] in string.whitespace and s[i+1] not in string.whitespace:
            collapsedString += " "
            i += 1
        #else do not add to collapsedstring, move to next original char
        else:
            i += 1
    return collapsedString

def openReplace(s1,s2):
    #helper function: add replacement string
    #if string to be replaced is ''
    stringReplace = ''
    for char in s1:
        stringReplace += s2 + char
    stringReplace += s2
    return stringReplace

def replace(s1, s2, s3):
    stringReplace = ''
    length = len(s2) #length of substring to check
    if length == 0:
        return openReplace(s1,s3)
    i = 0
    while (i < len(s1)-length): #stay in range
        #replace if substring1 = string 2
        if s1[i:i+length] == s2:
            stringReplace += s3
            i += length #jump over all replaced chars
        #ammend substring1[i] otherwise
        else:
            stringReplace += s1[i]
            i += 1
    #check end of string1 with same rules as above
    remaining = i - len(s1)
    if s1[remaining:] == s2:
        stringReplace += s3
    else:
        stringReplace += s1[remaining:]
    return stringReplace

def encodeOffset(s, d):
    encodedString = ''
    lowerLookup = string.ascii_lowercase
    upperLookup = string.ascii_uppercase
    d=d%26 #multiple loops through alphabet
    i = 0
    while (i < len(s)):
        if s[i].islower():
            #find index in list of lowercase letters
            searchIndex = string.ascii_lowercase.find(s[i])
            #Keep seach index less then length of list
            searchIndex = (searchIndex + d)%26
            #append index + d place from lowercase
            encodedString += string.ascii_lowercase[searchIndex]
        #same approach but for uppercase letters
        elif s[i].isupper():
            searchIndex = string.ascii_uppercase.find(s[i])
            searchIndex = (searchIndex + d)%26
            encodedString += string.ascii_uppercase[searchIndex]
        #append original if not lower or uppercase
        #i.e. if not a letter
        else:
            encodedString += s[i]
        i += 1
    return encodedString


def decodeOffset(s, d):
    decodedString = ''
    lowerLookup = string.ascii_lowercase
    upperLookup = string.ascii_uppercase
    d=d%26 #multiple loops through alphabet
    i = 0
    while (i < len(s)):
        if s[i].islower():
            #find index in list of lowercase letters
            searchIndex = string.ascii_lowercase.find(s[i])
            #Keep seach index less then length of list
            searchIndex = (searchIndex - d)%26
            #append index + d place from lowercase
            decodedString += string.ascii_lowercase[searchIndex]
        #same approach but for uppercase letters
        elif s[i].isupper():
            searchIndex = string.ascii_uppercase.find(s[i])
            searchIndex = (searchIndex - d)%26
            decodedString += string.ascii_uppercase[searchIndex]
        #append original if not lower or uppercase
        #i.e. if not a letter
        else:
            decodedString += s[i]
        i += 1
    return decodedString

def encrypt(msg, pwd):
    return 42

def decrypt(msg, pwd):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False)
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testRotateStringLeft():
    print("Testing rotateStringLeft()...", end="")
    assert(rotateStringLeft("abcde", 0) == "abcde")
    assert(rotateStringLeft("abcde", 1) == "bcdea")
    assert(rotateStringLeft("abcde", 2) == "cdeab")
    assert(rotateStringLeft("abcde", 3) == "deabc")
    assert(rotateStringLeft("abcde", 4) == "eabcd")
    assert(rotateStringLeft("abcde", 5) == "abcde")
    assert(rotateStringLeft("abcde", 25) == "abcde")
    assert(rotateStringLeft("abcde", 28) == "deabc")
    print("Passed!")

def testRotateStringRight():
    print("Testing rotateStringRight()...", end="")
    assert(rotateStringRight("abcde", 0) == "abcde")
    assert(rotateStringRight("abcde", 1) == "eabcd")
    assert(rotateStringRight("abcde", 2) == "deabc")
    assert(rotateStringRight("abcde", 3) == "cdeab")
    assert(rotateStringRight("abcde", 4) == "bcdea")
    assert(rotateStringRight("abcde", 5) == "abcde")
    assert(rotateStringRight("abcde", 25) == "abcde")
    assert(rotateStringRight("abcde", 28) == "cdeab")
    print("Passed!")

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("cba", "abcabcabc") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    assert(sameChars("","a") == False)
    print("Passed!")

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg", 4) == """\
a*b
c*de
fg""")
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters("\t \n&^#$") == "")
    noq = string.ascii_lowercase.replace('q','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    print("Passed!")

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")

def testReplace():
    print("Testing replace()...", end="")
    (s1, s2, s3) = ("abcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abcdeabcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("babababa", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abb", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "", "q")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "ab", "")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    print("Passed!")

def testEncodeOffset():
    print("Testing encodeOffset()...", end="")
    assert(encodeOffset("ACB", 1) == "BDC")
    assert(encodeOffset("ACB", 2) == "CED")
    assert(encodeOffset("XYZ", 1) == "YZA")
    assert(encodeOffset("ABC", -1) == "ZAB")
    assert(encodeOffset("ABC", -27) == "ZAB")
    assert(encodeOffset("Abc", -27) == "Zab")
    assert(encodeOffset("A2b#c", -27) == "Z2a#b")
    print("Passed!")

def testDecodeOffset():
    print("Testing decodeOffset()...", end="")
    assert(decodeOffset("BDC", 1) == "ACB")
    assert(decodeOffset("CED", 2) == "ACB")
    assert(decodeOffset("YZA", 1) == "XYZ")
    assert(decodeOffset("ZAB", -1) == "ABC")
    assert(decodeOffset("ZAB", -27) == "ABC")
    assert(decodeOffset("Zab", -27) == "Abc")
    assert(decodeOffset("Z2a#b", -27) == "A2b#c")
    print("Passed!")

def testEncrypt():
    print("Testing encrypt()...", end="")
    assert(encrypt("Go Team!", "azby") == "GNUCAL")
    assert(encrypt("a1m2a3z4i5n6g !?!?", "yes") == "YQSXMFE")
    assert(encrypt("", "wow") == "")
    assert(encrypt("Wow!", "AZBY") == "password must be all lowercase")
    print("Passed!")

def testDecrypt():
    print("Testing decrypt()...", end="")
    assert(decrypt("GNUCAL", "azby") == "GOTEAM")
    assert(decrypt("YQSXMFE", "yes") == "AMAZING")
    assert(decrypt("", "wow") == "")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testVowelCount()
    testInterleave()
    testHasBalancedParentheses()
    testRotateStringLeft()
    testRotateStringRight()
    testWordWrap()
    testLargestNumber()
    testLongestSubpalindrome()
    testLeastFrequentLetters()
    testSameChars()
    testMostFrequentLetters()
    testAreAnagrams()
    testCollapseWhitespace()
    testReplace()
    testEncodeOffset()
    testDecodeOffset()
    testEncrypt()
    testDecrypt()

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
