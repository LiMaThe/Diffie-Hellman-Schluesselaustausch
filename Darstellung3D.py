import matplotlib.pyplot as plt
import numpy as np
import Startpunkt as sp
import matplotlib.animation as animation
import squaremultiply as sm
import math

# ellitpische Kurve, Parameter:
a = 2
b = 5
p = 23

l= 4*sm.squareMultiply(a,3,p)+27*sm.squareMultiply(b,2,p)
if(l==0):
    print("Warnung: Bedingung für elliptische Kurve nicht erfüllt!")

# Darstellung erstellen
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

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

liste.append([None,None])
n = len(liste)
liste = list(map(lambda x: [x[0],x[1],0] if x[0] != None or x[1] != None else [0,0,1] ,liste))

liste = np.array(liste)


# Elliptische Kurve plotten mit scatter
Grafik =  ax.scatter(liste[:,0],liste[:,1],liste[:,2],c = "b")

# Startpunkt und Vielfache bis k*Q erzeugen
Q =  sp.startpunkt(a,b,p)

liste3 = [Q]
k = 12 

for i in range(2,k+1):
    Qneu = sm.doubleAdd2(i,Q,a,p)
    liste3.append(Qneu)

Tripel = list(map(lambda x: [x[0],x[1],0] if x[0] != None or x[1] != None else [0,0,1] ,liste3))

liste3 = np.array(Tripel)
print(liste3)
# Vielfache plotten
QWerte =  ax.plot(liste3[:0,0],liste3[:0,1],liste3[:0,2],"o-r")

def update(i):
    QWerte[0].set_xdata(liste3[:i+1,0])
    QWerte[0].set_ydata(liste3[:i+1,1])
    QWerte[0].set_3d_properties(liste3[:i+1,2])
    return QWerte

ani = animation.FuncAnimation(fig, update, frames=range(k), interval =  500)

plt.show()