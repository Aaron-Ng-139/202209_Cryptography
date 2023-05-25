# Encryption
import random

# My 4-bit s-box
inputX = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
outputY = [10,9,8,3,2,5,13,6,1,4,11,15,14,12,0,7] # Created by myself
# outputY = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7] # Textbook Example

# Random 5 round keys
# roundKeys = [51480, 5632, 5177, 16886, 21226]
roundKeys = [8124, 9645, 35912, 31504, 48138]

# Function to encrypt plaintext
def doEncrypt(plaintext_int):
    
    outputXOR_int = plaintext_int
    # For 4 rounds: XOR w/ round key, s-box, permute
    for j in range(4):
        # XOR w/ round key
        outputXOR_int = outputXOR_int ^ roundKeys[j]

        # Convert integer to binary
        outputXOR_bin = (bin(outputXOR_int)[2:]).zfill(16)
        # Split into groups of 4 groups of 4 bits each
        input = [
            int(outputXOR_bin[0:4], 2),
            int(outputXOR_bin[4:8], 2),
            int(outputXOR_bin[8:12], 2),
            int(outputXOR_bin[12:16], 2)]
        
        # Run through s-box
        for i in range(4):
            input[i] = (bin(outputY[input[i]])[2:]).zfill(4)

        # Permutation only during first 3 rounds
        if j < 3 :
            newInput = ["", "", "", ""]
            for i in range(4):
                for j in range(4):
                    newInput[j] = newInput[j] + input[i][j:j+1]
        
        # Turn 4 groups of 4 bits back into 16 bit int
        outputXOR_int = int(newInput[0] + newInput[1] + newInput[2] + newInput[3], 2)


    # XOR w/ round key one last time
    result = outputXOR_int ^ roundKeys[4]

    return result


# Main function

# Open file to output plaintext-ciphertext pairs
f = open("C:/Users/aaron/Downloads/CSI 4108 A2 Q2/pc_pairs.txt", "w")
# Write down round keys
roundKeys_str = ""
for key in roundKeys :
    roundKeys_str += str(key) + ","
f.write(roundKeys_str[:-1] + "\n")

for i in range (10000):
    # Randomly generate 16-bit plaintext
    rand_16bit_int = random.randrange(0, 65535)
    # Encrypt plaintext
    encrpyted_16bit_int = doEncrypt(rand_16bit_int)

    f.write(str(rand_16bit_int) + "," + str(encrpyted_16bit_int) + "\n")
    
f.close()

