import re

def numToWords(number):
    """ 
        Accepts a whole number from zero (0) to 1 million (1000000; without 
        commas for example: 1,000,000) and prints on screen the number in word form
    """
    print(numToWordsHelper(number))

def numToWordsHelper(number, accumulator = ""):
    """ 
        Accepts a number and returns the number in word form

        Args:
            number (int): The number to convert.
            accumulator (string): Variable used by the function to 
                accumulate the result.

        Returns:
            string: The converted number.
    """
    if number == 0:
        return "zero "
    elif number < 0:
        return (numToWordsHelper(number*-1, "negative "))
    elif number >= 1000000000:
        return numToWordsHelper(number%1000000000, accumulator + numToWordsHelper(int(number/1000000000)) + "billion ")
    elif number >= 1000000:
        return numToWordsHelper(number%1000000, accumulator + numToWordsHelper(int(number/1000000)) + "million ")
    elif number >= 1000:
        return numToWordsHelper(number%1000, accumulator + numToWordsHelper(int(number/1000)) + "thousand ")
    elif number >= 100:
        return numToWordsHelper(number%100, accumulator + numToWordsHelper(int(number/100)) + "hundred ")
    elif number > 29:
        return numToWordsHelper(number%10, accumulator + getNumPrefix(int(number/10)) + "ty ")
    elif number >= 20:
        return numToWordsHelper(number%10, accumulator + "twenty ")
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
    """
        Returns the prefix from numbers eg eigh in eigh(ty) or eigh(teen).
        
        Args:
            number (int): The number to get the prefix from.

        Returns:
            string: The prefix or None if invalid.
    """
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
    return

def wordsToNum(numberWord):
    """
        Accepts a number in word form (from zero to 1 million) and 
        returns it in numerical form Input must be in lowercase

        Args:
            numberWord (string): The number in word form.

        Returns:
            int: The converted number or None if the string has
                words
    """
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
        else:
            return
        number += holder
        holder = 0

    return number+holder

def getNumPrefixValue(word):
    """
        Accepts a prefix and returns the value.

        Args:
            word (string): The prefix to convert

        Returns:
            int: The value of the prefix.
    """
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

def wordsToCurrency(words, currency):
    """
        Accepts two arguments: the first argument is the 
        number in word form (from zero to 1 million) and
        the second argument is any of the following: JPY,
        PHP, USD. The function returns the number in words 
        to its numerical form with a prefix of the currency

        Args:
            words (string): The number to use.
            currency (string): The currency to use.

        Returns:
            string: The number with its currency.
    """
    if not re.match('JPY|PHP|USD', currency):
        return
    number = wordsToNum(words)
    if not number:
        return
    return currency + str(number)

def numberDelimited(number, delimiter, step):
    """
        Adds delimeters to a number

        Args:
            number (int): The number to delimit..
            delimeter (string): The character used to delimit the number.
            step (int): THe number of jumps when the delimeter will appear.

        Returns:
            string: The delimited number.
    """
    number = re.sub("(.{" + str(step) + "})", "\\1" + delimiter, str(number)[::-1], 0, re.DOTALL)[::-1]
    if number[0] == delimiter:
        number = number[1:]
    return number

