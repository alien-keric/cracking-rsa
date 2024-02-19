#cracking public key components from a id_rsa.pub
#Author alienX
#!/bin/python3

from Crypto.PublicKey import RSA
f = open("id_rsa.pub", "r")
key = RSA.importKey(f.read())
print(key.n)
print(key.e)
