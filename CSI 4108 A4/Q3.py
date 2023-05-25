import hashlib

# Same numbers from Q2
p = 166908634083704717798145075854598693430795653976206881916532608828523245603439447777998474622599284545048494242560507804735102709409703986040362817312076799114353981577032167701504568063038803431419114613244733449563523013267380463112265270185943953921441151075531877582602031507474581172785524192660063507483
q = 1429259239409870121351108700674303082924063653307
g = 164469706507664305012434282200621548271114912901268903258944708861891466838461582678631546121559698919927608206764121875848449875053917512129605472603418503968566860756289931662231944879982717529049771054336680014135498486973669545386421465365701305091524239826786519043109800326844313662648146264196146805022

x = 9325
y = pow(g, x, p)

# Signing message m1 from Q2
m1 = b'522346828557612'
k = 2098
k_inv = pow(k, -1, q)
r1 = pow(pow(g, k, p), 1, q)
s1 = pow( (int(hashlib.sha1(m1).hexdigest(), 16) + x*r1) * k_inv , 1, q)
signature1 = [r1,s1]

# Signing message m2
m2 = b'8161474912883'
r2 = pow(pow(g, k, p), 1, q)
s2 = pow( (int(hashlib.sha1(m2).hexdigest(), 16) + x*r2) * k_inv , 1, q)
signature2 = [r2,s2]

# By outputting the signatures, we see that r1 = r2
# print("sig1", signature1)
# print("sig2", signature2)

# Attacker can now learn k
hash_m1 = int(hashlib.sha1(m1).hexdigest(), 16)
hash_m2 = int(hashlib.sha1(m2).hexdigest(), 16)


print("k*(s2-s1) == hash_m2-hash_m1 is", pow(k * (s2 - s1), 1, q) == pow(hash_m2 - hash_m1, 1, q))
k_revealed = pow( hash_m2 - hash_m1 , 1, q) / pow( s2 - s1 , 1, q)
print(k_revealed)
# Unsure why this does not give the correct value of k even though the step before is correct

x_revealed = (k*s1 - hash_m1) / r1
print(x_revealed)
# Again unsure why it is giving the incorrect value when the equation is correct.

# But this shows that if k is reused, then the attacker can learn k and then your private key.
