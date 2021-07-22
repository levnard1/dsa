"""You may have heard of the infinite
monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the com-
plete works of William Shakespeare. Well, suppose we replace a monkey with a Python func-
tion. How long do you think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: 
                                          “methinks it is like a weasel”

You are not going to want to run this one in the browser, so fire up your favorite Python IDE. The
way we will simulate this is to write a function that generates a string that is 27 characters long
by choosing random letters from the 26 letters in the alphabet plus the space. We will write
another function that will score each generated string by comparing the randomly generated
string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct
we are done. If the letters are not correct then we will generate a whole new string. To make
it easier to follow your program’s progress this third function should print out the best string
generated so far and its score every 1000 tries.
"""
import random

genList = []

scoreCardDict  = {}

sentence = "methinks it is like a weasel"


def randomGenerate():
    alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',]
    

    for i in range(len(alphabetList)):
        genList.append(alphabetList[random.randint(0,26)])
    #print (genList)

def compareWeasel():
    
    score = 0
    
    sentenceList = list(sentence)
    #print (sentenceList)

    
    for i in range(27):
        if (genList[i] == sentenceList[i]):
            score += 1
			

    


def callerFunc():
    randomGenerate()
    compareWeasel()

    for i in range(999):
        if score == 27:
            print ("We won on the " + i + "th try!!!!")
            break
        else:
            scoreCardDict[score] = genList


            randomGenerate()
            compareWeasel()

    for key in scoreCardDict:
      print (key) 

callerFunc()





    


    

    





    
    













