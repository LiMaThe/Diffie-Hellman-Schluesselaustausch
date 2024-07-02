import numpy as np
import squaremultiply as sm
import Startpunkt as sp
import addition_punkte as ap
from copy import copy

if __name__ == "__main__":

    # Wähle eine Primzahl p für Fp:
    p = 154083204930662557781201849

    # Wähle Parameter a, b für elliptische Kurve y^2 = x^3 + a*x +b:
    a = 392734038478423048710
    b = 888388235883888883
    l= 4*sm.squareMultiply(a,3,p)+27*sm.squareMultiply(b,2,p)
    if(l==0):
        print("Warnung: Bedingung für elliptische Kurve nicht erfüllt!")

    # Erzeuge öffentlichen Punkt auf elliptischen Kurve:
    P =  sp.startpunkt(a,b,p)
    print("Startpunkt P ist:", P)

    # Wähle geheime Zahl m bzw geheime Zahl n:
    m = 3492059928347923 # Alice
    n = 9999276482387436 # Bob

    # Berechne jeweils öffentlichen Schlüssel m*P bzw n*P:
    mP = sm.doubleAdd2(m,P,a,p) # Alice
    print("m*P mit double&add:", mP)
    nP = sm.doubleAdd2(n,P,a,p) # Bob
    print("n*P mit double&add:", nP)

    # Berechne jeweils den geheimen Schlüssel:
    mnP = sm.doubleAdd2(m,nP,a,p) # Alice
    print("S=m*(nP) mit double&add:", mnP)
    nmP = sm.doubleAdd2(n,mP,a,p) # Bob
    print("S=n*(mP) mit double&add:", nmP) 

    """
    ############################### weitere Zahlen zum Testen: ###################################################

    p = 4101883650633306469376667499754908362247825865098673035333
    a = 3581901462183317683252070294477823918975914392619269996644
    b = 3581901462183317683252070294477823918975914392619269996644
    a = 298587239812
    b = 498458273 """

