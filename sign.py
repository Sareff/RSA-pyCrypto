from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# creation of signature
f = open('./plaintext.txt','rb')
plaintext = f.read(); f.close()
privatekey = RSA.importKey(open('./alisaprivatekey.txt','rb').read())
myhash = SHA.new(plaintext)
signature = PKCS1_v1_5.new(privatekey)
signature = signature.sign(myhash)


# signature encrypt
publickey = RSA.importKey(open('./bobpublickey.txt','rb').read())
cipherrsa = PKCS1_OAEP.new(publickey)
sig = cipherrsa.encrypt(signature[:128])
sig = sig + cipherrsa.encrypt(signature[128:])
f = open('./signature.txt','wb')
f.write(bytes(sig)); f.close()

