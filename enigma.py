## Title: enigma.py
## Description: Cypto project to build a simple enigma machine
## Author: Kyle Haptonstall
from random import shuffle
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#rotorList = [sorted(alphabet, key=lambda k: random.random()), sorted(alphabet, key=lambda k: random.random()), sorted(alphabet, key=lambda k: random.random())]
reflector = [['y','k'], ['j','m'], ['s','a'], ['r','e'], ['v','g'], ['b','u'], ['x','n'], ['c','i'], ['h','p'],['z','f'], ['q','t'], ['l','w'], ['d','o']]
rotorList = [['u', 'g', 'p', 'v', 'n', 'j', 'i', 'w', 'k', 's', 'a', 't', 'f', 'o', 'm', 'c', 'z', 'b', 'e', 'y', 'r', 'l', 'q', 'x', 'h', 'd'],
['l', 'a', 'u', 'r', 'y', 'n', 's', 'z', 'g', 'i', 'c', 'e', 'k', 'o', 'm', 'p', 'h', 'd', 'v', 'q', 'j', 'x', 'w', 'f', 't', 'b'],
['v', 'z', 'u', 'b', 'e', 'y', 'k', 'p', 'q', 'n', 'r', 'h', 'c', 'j', 't', 'o', 'a', 's', 'f', 'w', 'm', 'l', 'i', 'd', 'g', 'x']]
def enigmaC(rotors, positions, plainText):
    ##Set order of rotors
    rotorOne = rotorList[rotors[0] - 1]
    rotorTwo = rotorList[rotors[1] - 1]
    rotorThree = rotorList[rotors[2] - 1]
    #Set starting index for each rotor
    index_one = rotorOne.index(positions[0])
    index_two = rotorTwo.index(positions[1])
    index_three = rotorThree.index(positions[2])
    
    cipherText = ""


    for char in plainText:
        ##Rotate the first rotor each time
        rotorOne = rotorOne[(len(rotorOne) - 1):] + rotorOne[0: (len(rotorOne) - 2)]
        ## Then get the index of the letter of rotorOne on rotorTwo
        index = rotorTwo.index(rotorOne[index_one])
        ## Then get the letter that corresponds to the previous index
        letter = rotorThree[index]
        ## Search for this letter in the pairs and output its mapping
        pair = next(subl for subl in reflector if letter in subl)
        map = ""
        if pair[0] == letter:
            map = pair[1]
        else:
            map = pair[0]
        cipherText += map

    print(cipherText)

enigmaC([1,2,3], ['a','b','c'], "helloworld")
