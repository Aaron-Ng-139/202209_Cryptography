# Differential Attack

# My 4-bit s-box
inputX = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
outputY = [10,9,8,3,2,5,13,6,1,4,11,15,14,12,0,7] # Created by myself
# outputY = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7] # Textbook Example

# Open file containing plaintext-ciphertext pairs
f = open("C:/Users/aaron/Downloads/CSI 4108 A2 Q2/pc_pairs.txt", "r")
# First line has round keys
roundKeys = f.readline().split(',')
print(roundKeys)

# Populate dictionary of 256 possible partial subkeys
frequency = {}
for i in range(256):
    frequency[i] = 0

for i in range(9998) :
    # Grab ciphertext only and convert to binary
    raw = f.readline().split(',')
    if len(raw) < 2:
        print(raw)
        print(i)

    ciphertext_dec = int(raw[1])

    ciphertext_bin = (bin(int(ciphertext_dec))[2:]).zfill(16)

    # Split into groups of 4 groups of 4 bits each
    input_dec = [
        int(ciphertext_bin[0:4], 2),
        int(ciphertext_bin[4:8], 2),
        int(ciphertext_bin[8:12], 2),
        int(ciphertext_bin[12:16], 2)]

    # XOR ciphertext with all 256 possible partial subkeys
    for j in range(16) :
        # Run through s-box in reverse
        subkey_k51_k54 = outputY.index(input_dec[0] ^ j)
        for k in range(16) :
            # Run through s-box in reverse
            subkey_k55_k58 = outputY.index(input_dec[1] ^ k)
            if subkey_k55_k58 == 8 and subkey_k51_k54 == 8 : # if inverse s-box output is "1000"
                # Increment frequency
                partial_subkey = (16 * j) + k
                frequency[partial_subkey] = frequency[partial_subkey] + 1

for i in range(256):
    frequency[i] = frequency[i]/10000

# Output results
for i in range(16):
    for j in range(16):
        index = (16 * i) + j
        print(frequency[index], end=" ")
    print()

print()
maxvalue = max(frequency.values())
maxkey = max(frequency, key=frequency.get)
print(maxvalue)
print(maxkey)
