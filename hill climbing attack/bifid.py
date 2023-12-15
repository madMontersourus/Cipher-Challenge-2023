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
def bifidDecrypt(text,square,period):
    text = [text[i:i+period] for i in range(0, len(text), period)]

    plaintext = ""
    for each in text:
        coords = []
        for i in each:
            coord = np.array(np.where(square==i))
            coord = (coord.flatten()).tolist()
            for j in range(0,2):
                coords.append(coord[j])
        temp = coords[:len(coords)//2]
        temp2 = coords[len(coords)//2:]
        coords = [temp,temp2]
        for i in range(len(coords[0])):
            plaintext += square[coords[0][i]][coords[1][i]]
    return plaintext
margin = 1
period = 4
# set the parent key to a Polybius square with an unmixed alphabet
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
parentKey = np.array([['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']])
# set the best fitness to the fitness of the unmodified ciphertext
bestFitness = fitness(ciphertext,EngTet)
# set the counter to 0
count = 51
# while the counter is less than 10,000
while count < 50:
    # copy the parent key into a child key
    childKey = parentKey
    # randomly choose one of these modifications to the child key:
    rand1 = random.randint(0,4)
    rand2 = random.randint(0,4)
    rand3 = random.randint(0,4)
    rand4 = random.randint(0,4)
    choice = random.randint(0,5)
        # swap two randomly selected elements
    if choice == 0:
        temp = childKey[rand1][rand2]
        childKey[rand1][rand2] = childKey[rand3][rand4]
        childKey[rand3][rand4] = temp
        # swap two randomly selected rows
    elif choice == 1:
        childKey[[rand1,rand2]]=childKey[[rand2,rand1]]
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
    trial = bifidDecrypt(ciphertext,childKey)
    # calculate the new fitness of the new plaintext
    trialFitness = fitness(trial,EngTet)
    # if (the new fitness exceeds the best fitness) or
    # ((the new fitness exceed the best fitness minus the margin) and
    # (we roll a 1 on a 20-sided die))
    if trialFitness < bestFitness or (trialFitness-margin and random.randint == 20): 
        # copy the new fitness to the best fitness
        bestFitness = trialFitness
        # copy the child key into the parent key
        parentKey = childKey
        # set the counter to 0
        count = 0
    # increment the counter
    count += 1
    print(count)
# output the parent key
plaintext = bifidDecrypt("GRQSIISSADCPQQFUKHRQLEBVDWWSCPEY",parentKey,period)
print(plaintext)
print(parentKey)
