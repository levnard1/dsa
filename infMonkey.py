
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





    


    

    





    
    













