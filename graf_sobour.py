#!/usr/bin/env python3

import pylab as pl
from pylab import linspace, pi, plot, sin, cos, show

f=open("soubor-ux.txt", "r")
x=[]
y=[]
while 1:
    radek=f.readline()
    if radek=="":
        break
    cisla=radek.split()
    x.append(float(cisla[0]))
    y.append(float(cisla[1]))

plot(x,y)
pl.grid(True)
pl.title("Graf hodnot ze souboru")

pl.xlim(-10,10)
pl.ylim([-0.25,1.1])

pl.show()
