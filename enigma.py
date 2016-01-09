## Title: enigma.py
## Description: Cypto project to build a simple enigma machine
## Author: Kyle Haptonstall
from random import shuffle
import random

alphabet = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
rotorList = [[4, 17, 21, 5, 11, 12, 15, 16, 22, 20, 10, 1, 23, 3, 6, 8, 9, 14, 18, 2, 19, 0, 13, 7, 24, 25],
[2, 7, 14, 4, 13, 18, 15, 25, 6, 8, 10, 9, 24, 19, 22, 20, 5, 12, 0, 17, 11, 1, 3, 23, 16, 21],
[12, 6, 7, 10, 9, 22, 8, 16, 25, 19, 18, 13, 17, 4, 21, 20, 3, 23, 24, 2, 5, 1, 0, 15, 14, 11]]
reflector = [[10, 1], [0, 24], [16, 7], [21, 22], [5, 3], [2, 18], [9, 23], [11,
  8], [17, 4], [19, 25], [15, 6], [20, 14], [12, 13]]
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#rotorList = [sorted(alphabet, key=lambda k: random.random()), sorted(alphabet, key=lambda k: random.random()), sorted(alphabet, key=lambda k: random.random())]
#reflector = [['y','k'], ['j','m'], ['s','a'], ['r','e'], ['v','g'], ['b','u'], ['x','n'], ['c','i'], ['h','p'],['z','f'], ['q','t'], ['l','w'], ['d','o']]
#rotorList = [['u', 'g', 'p', 'v', 'n', 'j', 'i', 'w', 'k', 's', 'a', 't', 'f', 'o', 'm', 'c', 'z', 'b', 'e', 'y', 'r', 'l', 'q', 'x', 'h', 'd'],
#['l', 'a', 'u', 'r', 'y', 'n', 's', 'z', 'g', 'i', 'c', 'e', 'k', 'o', 'm', 'p', 'h', 'd', 'v', 'q', 'j', 'x', 'w', 'f', 't', 'b'],
#['v', 'z', 'u', 'b', 'e', 'y', 'k', 'p', 'q', 'n', 'r', 'h', 'c', 'j', 't', 'o', 'a', 's', 'f', 'w', 'm', 'l', 'i', 'd', 'g', 'x']]

def enigma(rotors, positions, plainText):
    position1 = positions[0]
    position2 = positions[1]
    position3 = positions[2]

    rotorOne = rotorList[rotors[0] - 1]
    rotorTwo = rotorList[rotors[1] - 1]
    rotorThree = rotorList[rotors[2] - 1]

    for char in plainText:
        var1 = (rotorOne[(char + position1) % 25] - position1) % 25
        print("Var1: ")
        print(var1)
        var2 = (rotorTwo[(var1 + position2) % 25] - position2) % 25
        #print((var1 + position2) % 25)
        #print(rotorTwo[(var1 + position2) % 25])
        #print(len(rotorTwo))
        print("Var2: ")
        print(var2)
        var3 = (rotorThree[(var2 + position3) % 25] - position3) % 25
        print("Var3: ")
        print(var3)

        pair = next(subl for subl in reflector if var3 in subl)
        mappedLetter = 0
        if pair[0] == var3:
            mappedLetter = pair[1]
        else:
            mappedLetter = pair[0]

        print("Mapped letter: ")
        print(mappedLetter)
        rotorOneI = getRotorInverse(rotorOne)
        rotorTwoI = getRotorInverse(rotorTwo)
        rotorThreeI = getRotorInverse(rotorThree)

        var3 = (rotorThreeI[(mappedLetter + position3) % 25] - position3) % 25
        print("Var3: ")
        print(var3)
        var2 = (rotorTwoI[(var3 + position2) % 25] - position2) % 25
        print("Var2: ")
        print(var2)
        var1 = (rotorOneI[(var1 + position1) % 25] - position1) % 25

        print("Final: ")
        print(var1)


def getRotorInverse(rotor):
    rotorInverse = [None] * len(rotor)
    for i in range(0, len(rotor)):
        rotorInverse[rotor[i]] = i
    return rotorInverse


enigma([1,2,3], [3,4,5], [6])



#enigmaC([1,2,3], ['a','b','c'], "helloworld")
#enigmaC([1,2,3], ['a','b','c'], "yicxjkzdtb")
