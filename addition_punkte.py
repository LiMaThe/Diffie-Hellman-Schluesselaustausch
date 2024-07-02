from sympy import mod_inverse
from copy import copy
from sympy import GF

##### [None,None] wird als der Nullpunkt deklariert!

def addition(P,Q,a,p):
    if (Q == [None,None]):
        return P
    if (P == [None,None]):
        return Q
    xp = P[0]
    yp = P[1]
    xq = Q[0]
    yq = Q[1]
    if  (P != Q)  and (xp == xq): #P != Q und xp = xq
        return [None,None]
    if (xp != xq): # P != Q und xp != xq
        k = (yp-yq) * mod_inverse((xp-xq),p) 
        xr = (k**2-xp-xq) % p
        yr = (-yp+k*(xp-xr)) % p
        return [xr,yr]
    if (P == Q)  and (yp != 0):  # P = Q und yp != 0 != yq
        k = (3*xp**2 + a)* mod_inverse((2*yp),p)
        xr = (k**2-2*xp) % p
        yr = (-yp+k*(xp-xr)) % p
        return [xr,yr]
    if (P == Q) and (yp == 0): # P = Q und yp = yq = 0
        return [None,None]

def primitivMult(n,Q,a,p):
    P = [None,None]
    for i in range (n):
        P = addition(P,Q,a,p)
    return P

