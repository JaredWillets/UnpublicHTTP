import rsa


def decrypt(message, PrivKey):

    return rsa.decrypt(message, PrivKey).decode('utf-8')

def encrypt(message, PubKey):
    
    encrypted = rsa.encrypt(message.encode('utf-8'), PubKey)

    return encrypted

PubKey, PrivKey = rsa.newkeys(numberOfBits)

