def numToWord(number):
    if number == 0:
        print("zero", end="");
    elif number >= 1000000:
        numToWord(int(number/1000000));
        print("million ", end="");
        numToWord(number%1000000);
    elif number >= 1000:
        numToWord(int(number/1000));
        print("thoushand ", end="");
        numToWord(number%1000);
    elif number >= 100:
        numToWord(int(number/100));
        print("hundred ", end="");
        numToWord(number%100);
    elif number > 20:
        printNumPrefix(int(number/10));
        print("ty ", end = "");
        numToWord(number%10);
    elif number == 20:
        print("twenty ", end="");
        numToWord(number%10);
    elif number > 12:
        printNumPrefix(number%10);
        print("ty ", end = "");
    elif number == 12:
        print("twelve ", end="");
    elif number == 11:
        print("eleven ", end="");
    elif number == 10:
        print("ten ", end="");
    elif number == 9:
        print("nine ", end="");
    elif number == 8:
        print("eight ", end="");
    elif number == 7:
        print("seven ", end="");
    elif number == 6:
        print("six ", end="");
    elif number == 5:
        print("five ", end="");
    elif number == 4:
        print("four ", end="");
    elif number == 3:
        print("three ", end="");
    elif number == 2:
        print("two ", end="");
    elif number == 1:
        print("one ", end="");

def printNumPrefix(number):
    if number == 9:
        print("nine ", end="");
    elif number == 8:
        print("eight", end="");
    elif number == 7:
        print("seven", end="");
    elif number == 6:
        print("six", end="");
    elif number == 5:
        print("fif", end="");
    elif number == 4:
        print("four", end="");
    elif number == 3:
        print("thir", end="");
