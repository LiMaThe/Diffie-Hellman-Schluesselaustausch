# Diffie-Hellman-Schluesselaustausch
Im Rahmen meiner Bachelorarbeit erstellte ich Pythonfunktionen, welche einen Schlüsselaustausch nach Diffie und Hellman mit elliptischen Kurven über einem endlichen Körper F<sub>p</sub> (p Primzahl) realisieren.
## Kurze Beschreibung der Dateien:
- additionPunkte: Bereitstellen einer Funktion, welche auf einer elliptischen Kurve y<sup>2</sup> = x<sup>3</sup> +ax+b über dem endlichen Körper F<sub>p</sub> zwei Punkte Q und P addiert.
- squaremultiply: Bereitstellen der Funktionen Square&Multiply, sowie Double&Add und Double&Add2 zum schnell Potenzieren bzw. Mutliplizieren von Punkten in F<sub>p</sub> bzw. Punkten der elliptischen Kurve.
- Startpunkt: Funktion zur Berechnung einer Wurzel einer Zahl a aus F<sub>p</sub>, sowie Funktion zur Berechnung eines beliebigen Punktes auf einer gegebenen elliptischen Kurve.
- Schluessel_erzeugen: Für gegebene elliptische Kurve und Primzahl p, wird ein Schlüssel nach dem Diffie-Hellman-Verfahren erzeugt.
- DarstellungKurven: Für verschiedene Werte von a und b für eine elliptische Kurve y<sup>2</sup> = x<sup>3</sup> +ax+b und eine Primzahl p für den Körper F<sub>p</sub> kann die ellpitische Kurve geplottet werden.
- Darstellung2D: Für eine gegebene elliptische Kurve über F<sub>p</sub>, einen Punkt Q und eine natürliche Zahl k werden die Werte 1*Q, 2*Q, 3*Q,..., k*Q  in der affinen Ebene (2D) mit Hilfe einer Animation visualisiert.
- Darstellung3D: Für eine gegebene elliptische Kurve über F<sub>p</sub>, einen Punkt Q und eine natürliche Zahl k werden die Werte 1*Q, 2*Q, 3*Q,..., k*Q  in der projektiven Ebene (3D) mit Hilfe einer Animation visualisiert.
