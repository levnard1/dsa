"""
Given a list of daily temperatures temperatures, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""
#this problem still isn't solved!

def swap(s: list, i: int, j: int) -> None:
    if i != j:
        s[i], s[j] = s[j], s[i]


def less(a, b, key=None):
    if key is None:
        return a < b
    else:
        return key(a) < key(b)

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
myTemperatures = [73,72,72,72,72,79]
expectedOutput = [1, 1, 4, 2, 1, 1, 0, 0]

def daily(tempList):

  output = []

  for i in range(len(tempList)):

    try:

      if tempList[i] < tempList[i+1]:
        output.append(i)
    except IndexError:
      output.append(0)
      

  print (output)



daily(temperatures)
daily(myTemperatures)




