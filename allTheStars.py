import random

def coinFlip():
    flipResult = random.randint(0,1)
    if flipResult == 0:
        return True
    else:
        return False

width  = 200
height = 100

currentString = ""

for y in range(height):
    for x in range(width):
        if coinFlip() == True:
            currentString = currentString+"*"
        else:
            currentString = currentString+" "
    print(currentString)
    currentString = ""
