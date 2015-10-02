#!/usr/bin/python
from Crypto.PublicKey import RSA



if __name__ == '__main__':
	with open('private.pem','r') as f:
		key = RSA.importKey(f.read())
	with open('ciphertext.bin', 'rb') as f:
		C = f.read()
	print key.decrypt(C)
