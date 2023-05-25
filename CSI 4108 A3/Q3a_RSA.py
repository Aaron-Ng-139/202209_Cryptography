# RSA.py
import sympy
import math
from time import perf_counter

# @@@@@@@@ STOLEN CODE to find linear congruence e*d = 1 mod phi_n @@@@@@@@
def fastlinearcongruencex(powx, divmodx, N, withstats=False):
   x, y, z = egcditerx(powx, N, withstats)
   if x > 1:
      powx//=x
      divmodx//=x
      N//=x
      if withstats == True:
        print(f"powx = {powx}, divmodx = {divmodx}, N = {N}")
      x, y, z = egcditerx(powx, N)
      if withstats == True:
        print(f"x = {x}, y = {y}, z = {z}")
   answer = (y*divmodx)%N
   if withstats == True:
      print(f"answer = {answer}")
   return answer
def egcditerx(a, b, withstats=False):
  s = 0
  r = b
  old_s = 1
  old_r = a
  while r!= 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    if withstats == True:
      print(f"quotient = {quotient}, old_r = {old_r}, r = {r}, old_s = {old_s}, s = {s}")
  if b != 0:
    bezout_t = quotient = (old_r - old_s * a) // b
    if withstats == True:
      print(f"bezout_t = {bezout_t}")
  else:
    bezout_t = 0
  if withstats == True:
    print("Bézout coefficients:", (old_s, bezout_t))
    print("greatest common divisor:", old_r)
  return old_r, old_s, bezout_t
# From https://stackoverflow.com/questions/63021828/solving-modular-linear-congruences-for-large-numbers


# Primes were generated with sympy.randprime(2, 2**1024)
p = 127663548718662547361919848343884377421626290136371265470302671757546740242245132007746750770200219763268914154934563136083945636947920855045403566773452294217622037069605937800532485450184343693089354135388047963902605023449631271330142882486203586925404102998214703056247273329025701766620187226375363634659
q = 112446812744605965096764157764792379212834764142955216660852412035932530186164196306569737380802945627192424817016182549283208702587538604282690272416245936098759417922340282718859013852072983434968836728457975006202669400429828175627001541767689847324215893220750272623276445714617097259533602847737075815787

# Finding Public and Private Key
n = p * q
phi_n = (p-1)*(q-1)
e = 65537
if math.gcd(e, phi_n) != 1:
    print("Incompatible e, please choose different primes")
d = fastlinearcongruencex(e, 1, phi_n)
key_public = [e, n]
key_private = d

# Encrpyting message m
m = 466921883457309
ciphertext = pow(m, key_public[0], key_public[1])
# ciphertext = (m**key_public[0]) % key_public[1]


t1_start = perf_counter()
# @@@@@@@ Decrypting message m with CRT @@@@@@@
dP = 1 * pow(e,-1,p-1)
dQ= 1 * pow(e,-1,q-1)
qInv= 1 * pow(q,-1,p)

m1 = pow(ciphertext,dP,p)
m2 = pow(ciphertext,dQ,q)
h = (qInv*(m1 - m2)) % p
m_rec = m2 + h*q
# @@@@@@@ From https://asecuritysite.com/rsa/rsa_crt3 @@@@@@@
t1_stop = perf_counter()
print(m_rec)
print("Elapsed time: ", t1_stop - t1_start)


# Decrypting message m without CRT
t2_start = perf_counter()
msg_decrypted = pow(ciphertext, key_private, key_public[1])
# Doing the decryption raw would take like 15-30 minutes
# msg_decrypted = (ciphertext**key_private) % key_public[1]
t2_stop = perf_counter()
print(msg_decrypted)
print(msg_decrypted == m)
print("Elapsed time: ", t2_stop - t2_start)

# We can see that the CRT implementation of decryption is 3-4 times faster
# than python's pow() function. Both if these are faster than doing the full
# exponentiation and then modulus which would take dozens of minutes
