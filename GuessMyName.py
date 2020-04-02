#!/usr/bin/env python
# coding: utf-8

# In[2]:


#GUESS MY NAME game
#TEST comment added on Github

#ANSWERS LIST nameList
nameList = [
    ["John", "m", "It rhymes with dawn."],
    ["Judith", "f", "I was in 'Life of Brian'."] ,
    ["Albert", "m", "I got eaten by a lion."] ,
    ["Victoria", "f", "I wore black a lot and rarely smiled."],
    ["Benazir", "f", "I was prime minister of Pakistan."],
    ["Takeshi", "m", "I had a castle in a gameshow on the telly."], 
    ["Emeline", "f", "I was a prominent Suffragette."],
    ["Seamus", "m", "It's Irish for James."],
    ["Fred", "m", "I'm in 'Step Up To The Plate' and 'First Dates'."],
    ["Nicole", "m", "I'm shamazing."],
    ["Jane", "f", "I liked swinging through the jungle with my boyfriend."], 
    ["Rita", "f", "I was a lovely parking attendant in a song."],
    ["Sue", "f", "I was friends with Rita, and Bob too."] ,
    ["Innes", "m", "I have children called Laurie and Seamus."],
    ["Raj", "m", "I am a newsagent in books by David Walliams."],
    ["Ding", "m", "I'm a Chinese snooker player and this is probably my surname."],
    ["Motsi", "f", "I'm a judge on Strictly."],
    ["Henrik", "m", "I'm Swedish and I played for Celtic."],
    ["Octavia", "f", "I could be somebody's 8th daughter, or maybe a car."],
    ["Laurie", "m", "I could be articulated."],
    ["Rumpelstiltskin", "m", "I can spin straw into gold."],
    ["Andy","m","I'm Scotland's best ever tennis player."],
    ["Bill","m","I'm one of the flowerpot men."],
    ["Mary","f","I'm a magical nanny."],
    ["Anne","f","I'm one of the Famous Five."],
    ["Dick","m","I'm one of the Famous Five."],
    ["Goldilocks","f","I'm a porridge thief."],
    ["Charlotte","f","I'm a little princess."],
    ["Meghan","f","I married a ginger prince."],
    ["Esther","f","I have a book to myself in the bible."],
    ["Mohammed","m","I'm the big cheese in Islam."],
    ["Martha","f","I do all the housework in Gilead"],
    ["Victor","m","I'm still game."],
    ["Robin","m","I visit your garden and I can get a bit fighty."],
    ["Iris","f","I help you to see."],
    ["George","m","I have a house in Budapest and a golden grand piano."],
    ["Severus","m","I'm good with potions."],
    ["Minerva","f","I'm Professor McGonagall."],
    ["Alfred","m","I burnt the cakes."],
    ["Joshua","m","I'm a tree. You too?"],
    ["Evelyn","f","I'm a whizz on the xylophone, the marimba and all the bangy, shaky things."],
    ["Margaret","f","I'm not for turning."],
    ["Eric","m","My best friend is Bert."],
    #["","",""],
]


#testing script for nameList entries and function calls
#prints full entry and all calls per entry
""" 
for x in range (len(nameList)) :
    testName = nameList[x][0]
    testshortGender = nameList[x][1]
    testGender = genderWord (testshortGender)
    testClue = nameList[x][2]
    testInitial = initCap (testName)
    testClueTwo = testName[1]
    testLen = len(nameList[x][0])
    print (testName, testshortGender, testGender, testClue, testInitial, testClueTwo, testLen)
    """

#FUNCTIONS

#import randint
from random import randint

#function to choose a random index from the names list
def chooseRand (lst) :
    index = randint (0, len(lst)-1)
    return (index)

# function to get real word to represent gender
def genderWord (letter) :
    if letter == "m" :
        return ("boy's")
    elif letter == "f" :
        return ("girl's")
    else :
        return (False)

# function to get the initial letter of the name with "a" or "an" in front
def initCap (strng) :
    capstrng = strng.capitalize()
    if capstrng in ["A", "E", "F", "H", "I", "L", "M", "N", "O", "R", "S", "U", "X"] :
        article = ("an")
    else :
        article = ("a")
    return (article + " " + capstrng[0])

#function to make guesses and answers lower case for easy comparison
def flatten (strng) :
    flatstrng = strng.lower()
    return (flatstrng)

#END FUNCTIONS

#WELCOME MESSAGE
print ("Welcome to GUESS MY NAME. You have 3 chances to guess my name.\n")

playAgain = "y"
while playAgain == "y" :

    #SET UP GAME VARS
    ansIndex = chooseRand (nameList)
    getName = nameList[ansIndex][0]
    shortGender = nameList[ansIndex][1]
    getGender = genderWord (shortGender)
    getClue = nameList[ansIndex][2]
    getInitial = initCap (getName)
    getClueTwo = getName[2]
    getLen = len(getName)

    #SHOW NAME FOR TESTING
    #print (getName)
    #print (getLen)

    #FIRST CLUE
    print ("My name starts with " + getInitial + " and is usually a " + getGender + " name.")
    print (getClue)

    tries = 0

    while tries < 3 :
        guess = input ("\nWhat's my name?")
        while len(guess) < 3 :
            guess = input ("Try again. My name has at least 3 letters. What's my name?")
        if flatten (guess) == flatten (getName) :
            print ("\n***Well done! You got it! My name is " + getName + ".***")
            break
        elif tries < 2 and flatten (guess)[1] == flatten (getName)[1] :
            print ("\nClose! You have the second letter correct.")
        else :
            print ("\nNope. That's not my name.")
        tries += 1
        if tries == 2 :
            print ("Have another clue. My name has " + str(getLen) + " letters and the third letter is " + getClueTwo.upper() + ".")
            

    print ("***GAME OVER***\n")
    playAgain = flatten (input ("Would you like to play again? y/n"))
    while playAgain != "y" and playAgain != "n" :
        playAgain = flatten (input ("Please type y for yes or n for no. Would you like to play again?"))
    if playAgain =="y" :
        print("\nGreat! ***NEW GAME***\n")

print ("\nThank you for playing. Have a nice day.")

