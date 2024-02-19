```
how to create a id_rsa key
**command:**
ssh-keygen -t rsa

NB: After you have gain access to the id_rsa key file you can use the following command if you want to use the key

command1: chmod 600 id_rsa
command2: ssh -i id_rsa root@localhost


NB: but incase if the id_rsa key is a protected by the password you can try to crack it with john

command: ssh2john id_rsa > rsa_hash.txt
command: hashcat rsa_hash.txt /usr/share/wordlists/rockyou.txt     OR john rsa_hash.txt /usr/share/wordlists/rockyou.txt
```



# HOW TO EXTRACT THE VALUE OF e and n from a public key
```
Assume we have been given a public key (id_rsa.pub), and we need to extract the value of 'e' and 'n'

where:
e: public exponent(by default is 65537)
n: modulus (which is the result of p*q)
p:where q is a large prime number
q: where p is a large prime number 

WHERE:The public key in RSA is represented as (n, e), where 'n' is the modulus and 'e' is the public exponent

	WHILE
WHERE:The private key, on the other hand, consists of the modulus 'n' and a private exponent 'd', which is kept secret

NB:The mathematical relationship between 'e', 'd', and 'n' is such that encrypting with the public key can only be efficiently reversed using the private key.



NOW ASSUME WE HAVE A id_rsa.pub(public key and we want to break it, which means we can use python or python3 or any other language to try to extract and crack  the value of 'n' and 'e' first)

#!/bin/python3
# This pieve of code can help us to crack the value of n and e we just need the `pycryptodome`library
from Crypto.PublicKey import RSA
f = open("id_rsa.pub", "r")
key = RSA.importKey(f.read())
print(key.n) # prints the value of n(modulus)
print(key.e) # print the value of e (exponential)



After we have managed  to extract these two values we now need to get the value of 'p' and 'q' from this two value we have obtained and in order to achieve this we need:

QN:Factorize n into prime numbers p and q (Fermats Factorization method)

NB: we can use a script below to calculate value of p,q,d and private key
```