SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print("Do you wish to \"encrypt\", \"decrypt\" or \"brute\" the message?")
        mode = input().lower()
        if mode in ["encrypt", "e", "decrypt", "d", "brute", "b"]:
            return mode
        else:
            print("You input either \"encrypt\" , \"decrypt\" , \"brute\" , \"e\" , \"d\" or \"b\".")


def getMessage():
    print("Please input the message.")
    return input()


def getKey():
    key = 0
    while True:
        print("please enter a key, which is between 1~%s" %MAX_KEY_SIZE)
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
    
    return translated


mode = getMode()
message = getMessage()
if mode[0] != "b":
    key = getKey()
print("Your translated is:")
if mode[0] != "b":
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage(mode, message, key))