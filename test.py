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

def wordsToNum(numberWord):
    numberWord = numberWord.lower()
    words = re.split("\W+", numberWord); 
    holder = 0
    number = 0
    for word in words:
        if word == "":
            continue
        elif word == "zero" and len(words) == 3: #ensure zero is the only word
            return 0
        elif word == "one":
            holder += 1
            continue
        elif word == "two":
            holder += 2
            continue
        elif word == "three":
            holder += 3
            continue
        elif word == "four":
            holder += 4
            continue
        elif word == "five":
            holder += 5
            continue
        elif word == "six":
            holder += 6
            continue
        elif word == "seven":
            holder += 7
            continue
        elif word == "eight":
            holder += 8
            continue
        elif word == "nine":
            holder += 9
            continue
        elif word == "ten":
            holder += 10
            continue
        elif word == "hundred":
            holder *= 100
            continue
        elif word == "thousand":
            holder *= 1000
        elif word == "million":
            holder *= 1000000
        elif word == "eleven":
            holder += 11
            continue
        elif word == "twelve":
            holder += 12
            continue
        elif word == "twenty":
            holder += 20
            continue
        elif re.match(".*(ty|teen)", word):
            prefix = getNumPrefixValue(re.match(".*(?=ty|teen)", word).group(0))
            if not prefix:
                return
            if word[-1] == "n":
                holder += prefix + 10
            else:
                holder += prefix * 10
            continue
        number += holder
        holder = 0

    return number+holder

def getNumPrefixValue(word):
    if word == "nine":
        return 9
    elif word == "eigh":
        return 8
    elif word == "seven":
        return 7
    elif word == "six":
        return 6
    elif word == "fif":
        return 5
    elif word == "four":
        return 4
    elif word == "thir":
        return 3


print(wordsToNum("twelve million seven thousand eleven"))
