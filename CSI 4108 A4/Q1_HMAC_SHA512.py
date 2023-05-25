import hashlib
import hmac

message = "I am using this input string to test my own implementation of HMAC-SHA-512."
KEY = "CSI 4108" # Key of my choosing
ipad = "00110110"
opad = "01011100"

### My HMAC implementation ###
# Binary to string function stolen from stackoverflow
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# Convert key to binary
k = ''.join(format(i, '08b') for i in bytearray(KEY, encoding ='utf-8'))

# Pad key to be 512 bits in length (output size of SHA-512)
k = k.zfill(512)
# Repeat ipad & opad 512/8 = 64 times
ipad = ipad * 64
opad = opad * 64

# Convert string to integer, XOR operations, then convert back to binary
k_ipad = bin(int(k, 2) ^ int(ipad, 2))[2:]
k_opad = bin(int(k, 2) ^ int(opad, 2))[2:]

# Refill lost zeroes from integer conversion
k_ipad = k_ipad.zfill(512)
k_opad = k_opad.zfill(512)

# Convert binary into utf-8 strings
k_ipad = decode_binary_string(k_ipad).encode('utf-8')
k_opad = decode_binary_string(k_opad).encode('utf-8')

# Hashing
sha512 = hashlib.sha512()
sha512.update(k_ipad + message.encode('utf-8'))
sha512_v2 = hashlib.sha512()
sha512_v2.update(k_opad + sha512.digest())
print(sha512_v2.digest())



### Python library HMAC implementation ###
h = hmac.new(KEY.encode(), message.encode(), hashlib.sha512).digest()
print(h)
# They are different so I am not sure what I've done wrong