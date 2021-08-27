import rsa

numberOfBits = int(input('Please name a number of bits that should be used for this key (4096): '))
if numberOfBits == 0:
    numberOfBits = 4096