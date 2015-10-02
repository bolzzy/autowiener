#!/usr/bin/env python

#Feil format? openssl rsa -pubin -in <filename> -RSAPublicKey_out

import sys, getopt
import rsa as RSA2 

sys.path.append('rsa-wiener-attack-master')
from RSAwienerHacker import hack_RSA
sys.path.append('rsatool-master')
from rsatool import RSA

def getPubKey(p):
    try:
        rsa = RSA2.PublicKey.load_pkcs1(p, format='PEM')
    except:
        print "\n\nFeil format? openssl rsa -pubin -in <filename> -RSAPublicKey_out\n\n"
        sys.exit(2)
    N = rsa.n
    e = rsa.e
    return (e, N)

def get_private_from_public(e,n): 
    d = hack_RSA(e, n)
    print "\nYou got the d-_-d-->    ", d, "\n\n"
    rsa = RSA(n=n,d=d,e=e)

    data = rsa.to_pem()
    print data
    fb = open('private.pem', 'wb')
    fb.write(data)
    fb.close()
   
def main(argv):
    pubKey = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'small_d_rsa.py -i <publicKey.pem>'
        sys.exit(2)

    if not argv:
        print 'small_d_rsa.py -i <publicKey.pem>lol'
        sys.exit(2)

    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            print 'small_d_rsa.py -i <publicKey.pem>'                     
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
           try:
               file = open(arg, 'r')
           except:
               print "Finner ikke filen ", arg
               sys.exit(2)

           file2 = file.read()
           print file2
           e, N = getPubKey(file2)
           get_private_from_public(e, N)
        else:
            print "lol"

if __name__ == '__main__':
    main(sys.argv[1:])


   
