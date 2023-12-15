import random
import json
import numpy as np
ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")
EngTet = dict(json.loads(open("English-frequency.json","r").read()))
def tetragrams(text):
    TetFreq = {}
    count = 0
    for i in range (len(text)-3):
        count += 1
        if text[i:i+4] in TetFreq:
            TetFreq[text[i:i+4]] += 1
        else:
            TetFreq.update({f"{text[i:i+4]}":1}) 
    for each in TetFreq:
        TetFreq[each] = TetFreq[each]/count
    return TetFreq
def fitness(text,EngTet):
    CTTet = tetragrams(text)
    fitness = 0
    for each in CTTet:
        if each in EngTet:
            fitness += (CTTet[each]-EngTet[each])**2/EngTet[each]
    return(fitness)
def bifidDecrypt(text,square):
    coords = []
    for each in text:
        coord = np.array(np.where(square==each)).tolist()
        for i in range(0,2):
            num = ("".join(str(coord[i])).replace("[","")).replace("]","")
            if num != "":
                coord[i] = int(num)
        coords.append(coord)
        coords = [x for x in coords if x != [[],[]]]

# set the parent key to a Polybius square with an unmixed alphabet
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
parentKey = np.array([['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']])
bifidDecrypt(ciphertext,parentKey)
# set the best fitness to the fitness of the unmodified ciphertext
bestFitness = fitness(ciphertext,EngTet)
print(bestFitness)
# set the counter to 0
count = 0
# while the counter is less than 10,000
while count > 10000:
    # copy the parent key into a child key
    childKey = parentKey
    # randomly choose one of these modifications to the child key:
    rand1 = random.randint(0,5)
    rand2 = random.randint(0,5)
    rand3 = random.randint(0,5)
    rand4 = random.randint(0,5)
    choice = random.randint(0,6)
        # swap two randomly selected elements
    if choice == 0:
        temp = childKey[rand1][rand2]
        childKey[rand1][rand2] = childKey[rand3][rand4]
        childKey[rand3][rand4] = temp
        # swap two randomly selected rows
    elif choice == 1:
        childKey[rand1][rand2] = childKey[rand2][rand1]
        # swap two randomly selected columns
    elif choice == 2:
        childKey[:,[rand1,rand2]] = childKey[:,[rand2,rand1]]
        # flip the square around the diagonal that runs from upper left to lower right
    elif choice == 3:
        childKey = np.flip(childKey,axis=0)
        childKey = np.rot90(childKey)
        # flip the square vertically
    elif choice == 4:
        childKey = np.flip(childKey,axis=0)
        # flip the square horizontally
    elif choice == 5:
        childKey = np.flip(childKey,axis=1)
    # decipher the ciphertext with the child key to find a new plaintext
    # calculate the new fitness of the new plaintext
    # if (the new fitness exceeds the best fitness) or
    # ((the new fitness exceed the best fitness minus the margin) and
    # (we roll a 1 on a 20-sided die))
        # copy the new fitness to the best fitness
        # copy the child key into the parent key
        # set the counter to 0
    # increment the counter
# output the parent key
