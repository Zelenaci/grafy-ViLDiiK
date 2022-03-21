from tkinter import *
from tkinter import messagebox
import pylab as pl
from pylab import linspace, pi, plot, sin, cos, show

okno = Tk()
okno.config(padx=10,pady=10)
okno.title("Cosinus - graf")

fceMin=StringVar()
fceMax=StringVar()
fceVzorky=StringVar()

fceFrame=LabelFrame(okno, text="Parametry", padx=5, pady=5)
fceFrame.grid(column=0,row=0, sticky=W+E)
fceFrame.grid_columnconfigure(1,weight=1)
fceMin.set("Od")
fceMax.set("Do")
fceVzorky.set("Vzorků")
Entry(fceFrame, textvariable=fceMin, width=7).grid(column=1, row=0, sticky=E)
Entry(fceFrame, textvariable=fceMax, width=7).grid(column=1, row=1, sticky=E)
Entry(fceFrame, textvariable=fceVzorky, width=7).grid(column=1,row=2, sticky=E)

def cosGraf():
    try:    
        od=float( fceMin.get())
        do=float( fceMax.get())
        vzorky=int( fceVzorky.get())
        x=pl.linspace(od,do,vzorky)
        y=pl.cos(x)

        pl.plot(x,y)
        pl.xlabel("x")
        pl.ylabel("cos x")
        pl.grid(True)
        pl.show()
    except:
        pass

Button(okno, text="Vytvoř graf",command=cosGraf).grid(column=1,row=0, sticky=W+E+N+S)


okno.mainloop()