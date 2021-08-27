import rsa

def decrypt(message):

    PrivKey = rsa.PrivateKey.load_pkcs1(open('PrivKey','rb').read())

    return rsa.decrypt(message, PrivKey).decode('utf-8')

def encrypt(message):

    PubKey = rsa.PublicKey.load_pkcs1(open('PubKey','rb').read())
    
    encrypted = rsa.encrypt(message.encode('utf-8'), PubKey)

    return encrypted