from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# decryption session key
privatekey = RSA.importKey(open('./bobprivatekey.txt','rb').read())
cipherrsa = PKCS1_OAEP.new(privatekey)
f = open('./sessionkey.txt','rb')
sessionkey = f.read(); f.close()
sessionkey = cipherrsa.decrypt(sessionkey)

# decryption message
f = open('./plaintext.txt','rb')
ciphertext = f.read(); f.close()
iv = ciphertext[:16]
obj = AES.new(sessionkey, AES.MODE_CFB, iv)
plaintext = obj.decrypt(ciphertext)
plaintext = plaintext[16:]
f = open('./plaintext.txt','wb')
f.write(bytes(plaintext)); f.close()

