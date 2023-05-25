# Elgamal.py

# Global Public Elements
PRIME_Q = 89
PRIM_ROOT = 13

# Key Generation by Alice
X_A = 12    # X_A < 89 - 1
Y_A = (PRIM_ROOT**X_A) % PRIME_Q
key_public = [PRIME_Q, PRIM_ROOT, Y_A]
key_private = X_A
# Check
print("Alice's Public Key:")
print(key_public)

# Encryption by Bob with Alice's Public Key
m1 = 56     # 56 < 89
k = 37      # 37 < 89
K = (Y_A**k) % PRIME_Q
C1 = (PRIM_ROOT**k) % PRIME_Q
C2 = (K * m1) % PRIME_Q
ciphertext = [C1, C2]
# Check
print("Bob encrypts m1 with Alice's Public Key. The ciphertext is:")
print(ciphertext)

# Decryption by Alice with Alice's Private Key
K_m1 = (C1**X_A) % PRIME_Q
plaintext = (C2 * (pow(K_m1, -1, PRIME_Q))) % PRIME_Q
if K == K_m1 :
    print("K value is correct. K = " + str(K_m1))
if plaintext == m1 :
    print("m1 successfully recovered. m1 = " + str(plaintext))

# Finding m2
# ----------------------------

# m2 = ( (C21)^(-1) * C22 * M1 ) mod q

# X_A = 12
# Y_A = 13^12 mod 89 = 22
# K = 22^37 mod 89 = 81
# C11 = alpha^k mod q = 13^37 mod 89 = 29
# C12 = C11 = 29

# C21 = (K * m1) mod q = (81 * 56) mod 89 = 86
# (C21)^(-1) = 59
# C22 = (K * m2) mod q = (81 * m2) mod 89 = ??

# m2 = ( (C21)^(-1) * C22 * M1 ) mod 89
# m2 = ( 59 * C22 * 56 ) mod 89
# m2 = ( 3304 * C22 ) mod 89
# Therefore, m2 = ( 11 * C22 ) mod 89
# Since the ciphertext is not given, m2 is not assigned an integer value