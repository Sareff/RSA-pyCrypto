from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# decryption signature
f = open('./signature.txt','rb')
signature = f.read(); f.close()
privatekey = RSA.importKey(open('./bobprivatekey.txt','rb').read())
cipherrsa = PKCS1_OAEP.new(privatekey)
sig = cipherrsa.decrypt(signature[:256])
sig = sig + cipherrsa.decrypt(signature[256:])
# signature verification
f = open('./plaintext.txt','rb')
plaintext = f.read(); f.close()
publickey = RSA.importKey(open('./alisapublickey.txt','rb').read())
myhash = SHA.new(plaintext)
signature = PKCS1_v1_5.new(publickey)
test = signature.verify(myhash, sig)

