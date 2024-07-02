import addition_punkte as ap

def binary(m):
    liste = []
    while (m != 0):
        z = m & 1
        liste.append(int(z))
        m = m >> 1
    return liste

def squareMultiply(a,d,p): # Berechnet a^d mod p
    liste = binary(d)
    if liste[0] == 1:
        y = a % p
    else:
        y = 1
    x = a % p
    for di in liste[1:]:
        x = x**2 % p
        if (di == 1):
            y = (y * x) % p
    return y

def doubleAdd(d,a,p): #Berechnet d*a mod p
    liste = binary(d)
    if liste[0] == 1:
        y = a % p
    else:
        y = 0
    x = a % p
    for di in liste[1:]:
        x = 2*x % p
        if (di == 1):
            y = (y+ x) % p
    return y

def doubleAdd2(d,P,a,p): #Berechnet d * P wobei P ein Punkt auf der Ell. Kurve E_{a,b} über dem Körper Fp.
    liste = binary(d)
    if liste[0] == 1:
        y = P
    else:
        y = [None,None]
    for di in liste[1:]:
        P = ap.primitivMult(2,P,a,p)
        if (di == 1):
            y = ap.addition(y,P,a,p)
    return y
