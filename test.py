import re

def numToWords(number, accumulator = ""):
    if number == 0:
        return "zero "
    elif number < 0:
        return (numToWord(number*-1, "negative "))
    elif number >= 1000000000:
        return numToWord(number%1000000000, accumulator + numToWord(int(number/1000000000)) + "billion ")
    elif number >= 1000000:
        return numToWord(number%1000000, accumulator + numToWord(int(number/1000000)) + "million ")
    elif number >= 1000:
        return numToWord(number%1000, accumulator + numToWord(int(number/1000)) + "thousand ")
    elif number >= 100:
        return numToWord(number%100, accumulator + numToWord(int(number/100)) + "hundred ")
    elif number > 29:
        return numToWord(number%10, accumulator + getNumPrefix(int(number/10)) + "ty ")
    elif number >= 20:
        return numToWord(number%10, accumulator + "twenty ")
    elif number > 12:
        return accumulator+ getNumPrefix(number%10) + "teen "
    elif number == 12:
        return accumulator + "twelve "
    elif number == 11:
        return accumulator + "eleven "
    elif number == 10:
        return accumulator + "ten "
    elif number == 9:
        return accumulator + "nine "
    elif number == 8:
        return accumulator + "eight "
    elif number == 7:
        return accumulator + "seven "
    elif number == 6:
        return accumulator + "six "
    elif number == 5:
        return accumulator + "five "
    elif number == 4:
        return accumulator + "four "
    elif number == 3:
        return accumulator + "three "
    elif number == 2:
        return accumulator + "two "
    elif number == 1:
        return accumulator + "one "

def getNumPrefix(number):
    if number == 9:
        return "nine"
    elif number == 8:
        return "eigh"
    elif number == 7:
        return "seven"
    elif number == 6:
        return "six"
    elif number == 5:
        return "fif"
    elif number == 4:
        return "four"
    elif number == 3:
        return "thir"
    return ""

