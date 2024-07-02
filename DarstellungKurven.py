import matplotlib.pyplot as plt
import numpy as np
import Startpunkt as sp
import matplotlib.animation as animation
import squaremultiply as sm
import math

# ellitpische Kurve, Parameter:
a = 35
b = 11
p = 97

l= 4*sm.squareMultiply(a,3,p)+27*sm.squareMultiply(b,2,p)
if(l==0):
    print("Warnung: Bedingung für elliptische Kurve nicht erfüllt!")

# Darstellung erstellen
fig, ax = plt.subplots()

plt.grid() #Grid wird angezeigt

# Alle Punkte der eliptischen Kurve erzeugen
liste = []

for x in range (0,p):
    y2 = (x**3 + a*x +b) % p
    yp = sp.wurzel(y2,p)
    if yp != None:
        ym = p - yp
        liste.append([x,yp])
        liste.append([x,ym])

n = len(liste)
liste = np.array(liste)

# Elliptische Kurve plotten mit scatter
fisch =  plt.scatter(liste[:,0],liste[:,1],c = "b")

plt.show()