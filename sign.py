from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha265
import random


def sign(m):
	
	#Your code here
    G = secp256k1.G
    n = secp256k1.n
    
 
    d = random.SystemRandom().randint(1,n-1)
    
    #generate public key
	public_key = keys.get_public_key(d, G)
    
    x1=public_key.x
    y1=public_key.y
    
	#generate signature
	#Your code here
	r = pow(x1,1,n)
    if (r==0):
        
    z = sha256( m )
	s = pow(d,-1,n)* pow(z+rd,1,n)

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )