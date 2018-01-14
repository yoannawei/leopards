# this program determines if Jay is an egg

def isJayanEgg(status):
    if status > 9:
        return True
    else:
        return False

def printStatus(input):
    if input == True:
        print("Jay is an egg")
    else:
        print("Jay is not an egg")

def timeOftheMonth(mood):
    if mood == "mad" or mood == "angry":
        return True
    else:
        return False

def printTimeofMonth(status):
    if status == True:
        print("It is this time of the month")
    else:
        print("It is not yet this time the month")

userMood = input("WHat's your current mood?")
printTimeofMonth(timeOftheMonth(userMood.lower()))

userNum = input("What's your lucky number?")
printStatus(isJayanEgg(int(userNum)))




