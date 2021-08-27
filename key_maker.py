import rsa

numberOfBits = int(input('Please name a number of bits that should be used for this key (4096): '))
if numberOfBits == 0:
    numberOfBits = 4096

PubKey, PrivKey = rsa.newkeys(numberOfBits)

priv_key_file = open("PrivKey", 'w')
priv_key_file.write(PrivKey.save_pkcs1().decode('utf-8'))
priv_key_file.close()
pub_key_file = open("PubKey", 'w')
pub_key_file.write(PubKey.save_pkcs1().decode('utf-8'))
pub_key_file.close()