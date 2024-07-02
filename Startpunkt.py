import numpy as np
import squaremultiply as sm


####################### Funktionen zum Wurzel ziehen modulo p #################################

def Zerlegung (m):
# m = 2^e * q
    e = 0
    q = m
    while(q % 2 == 0):
        e = e+1
        q = m // 2**e
    return e, q

def GruppeG(p,q):  # Gegeben Zp*. p-1 = 2^e * q. Gruppe G in der die Elemente m^q sind mit m element Zp*.
    liste = np.zeros(p-1)
    for i in range(p-1):
        liste[i] = ((i+1)**q % p)
    return liste

def Erzeuger(p,q):
    for i in range(2,p):
        if (sm.squareMultiply(i,(p-1)//2,p) == p-1):
            z = sm.squareMultiply(i,q,p)
            return z

def ordnung(b,p):
    ei = 0
    while((sm.squareMultiply(b,2**ei,p)) != 1):
        ei = ei + 1
    return ei

def wurzel(a,p):
    if a % p == 0:
        return 0
    e,q = Zerlegung(p-1)
    x = sm.squareMultiply(a,(q+1)//2,p)
    b = sm.squareMultiply(a,q,p)
    z = Erzeuger(p,q)
    ei = ordnung(b,p)
    while(ei != 0 and ei != e):
        k = 2**(e-ei-1)
        x = (x* sm.squareMultiply(z,k,p) ) % p
        b = (b* sm.squareMultiply(z,k*2,p)) % p
        ei = ordnung(b,p)
    if ei == 0:
        return x               
    elif ei == e:
        return None

############################ Punkt auf elliptischen Kurve finden #############################

# elliptic curve: y^2 = x^3 + a * x + b

def startpunkt(a,b,p):
    for x in range(p//2,p):
        y2 =( x**3 +a*x +b ) %p
        y = wurzel(y2,p)
        if (y != None):
            return [x,y]
        


################## Beispiel Wurzel##################################################################

if __name__ == "__main__":
    p = 154083204930662557781201849  # hier Primzahl eingeben
    #p = 13
    print("Die Primzahl ist:{}".format(p))

    e,q = Zerlegung(p-1)
    q = int(q)
    print("{} ist 2^e * q mit e={} und q={}:".format(p-1,e,q))

    k=9846823490
    x = wurzel(k,p)
    print("Wurzel aus {} mod {} ist: {}".format(k,"p",x))

    if(x!= None):
        l=sm.squareMultiply(x,2,p)
        print("Probe: {}^2 mod {} = {}" .format(x,"p",l))

    ################################# Beispiel Startpunkt###################################################

    a=5
    b=3
    print("Die elliptische Kurve ist:y^2=x^3+{}x+{}".format(a,b))
    [x,y] = startpunkt(a,b,p)
    print("Ein Startpunkt auf der elliptischen Kurve mit a = {} und b = {} mod p ist: {}".format(a,b,[x,y]))