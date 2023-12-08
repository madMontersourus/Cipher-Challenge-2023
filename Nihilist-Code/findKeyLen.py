import numpy as np
from collections import Counter
import json

result_dict = {}

# Iterate through all possible combinations
for tens1 in range(1, 6):
    for ones1 in range(1, 6):
        for tens2 in range(1, 6):
            for ones2 in range(1, 6):
                # Form two 2-digit numbers
                num1 = 10 * tens1 + ones1
                num2 = 10 * tens2 + ones2

                # Calculate the sum of the two numbers
                total = str(num1 + num2)

                # Store the combination in the dictionary
                if total in result_dict:
                    try:
                        result_dict[total].index(str(num1))
                    except ValueError:
                        result_dict[total].append(str(num1))
                    try:
                        result_dict[total].index(str(num2))
                    except ValueError:
                        result_dict[total].append(str(num2))                      
                else:
                    result_dict[total] = [str(num1), str(num2)]
with open("nihilist-frequency.json","w") as fp:
    json.dump(result_dict, fp)


# Print the results
ciphertext = open("Nihilist-Code/nihilist-ciphertext.txt","r").read()
ciphertext = ciphertext.split(" ")
ciphertext = ciphertext[:1491]
ciphertext = np.reshape(ciphertext, (213,7))
ciphertext = np.rot90(ciphertext)

"""keySus = "44"
column = ciphertext[4].tolist()
for each in column:
    try:

        print("key not possible")
        exit()
print("key possible")"""