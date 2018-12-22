from Tkinter import *
import os

#window
root = Tk()
root.wm_title("Skontorechner")

#vars
summe=DoubleVar()
a=DoubleVar()
b=DoubleVar()
c=DoubleVar()
d=DoubleVar()
a.set(0)
b.set(0)
c.set(0)
d.set(0)
summe.set(0)
skonto2=DoubleVar()
skonto3=DoubleVar()

#functions

def valiMake(value):
	try:
		float(value)
	except:
		return False
	else:
		makeSkonto(value)
		return True

def valia(value):
	try:
		float(value)
	except:
		return False
	else:
		summe.set("{:.2f}".format(float(value)+b.get()+c.get()+d.get(),2))
		return True
def valib(value):
	try:
		float(value)
	except:
		return False
	else:
		summe.set("{:.2f}".format(a.get()+float(value)+c.get()+d.get(),2))
		return True
def valic(value):
	try:
		float(value)
	except:
		return False
	else:
		summe.set("{:.2f}".format(a.get()+b.get()+float(value)+d.get(),2))
		return True

def valid(value):
	try:
		float(value)
	except:
		return False
	else:
		summe.set("{:.2f}".format(a.get()+b.get()+c.get()+float(value),2))
		return True

def makeSkonto(value):
	skonto2.set("{:.2f}".format(round(0.98*float(value),2)))
	skonto3.set("{:.2f}".format(round(0.97*float(value),2)))

def reset():
	a.set(0)
	b.set(0)
	c.set(0)
	d.set(0)
	summe.set(0)

valiMakeD=(root.register(valiMake),'%P')
valiDa=(root.register(valia),'%P')
valiDb=(root.register(valib),'%P')
valiDc=(root.register(valic),'%P')
valiDd=(root.register(valid),'%P')

#entries
#main
Label(root,text="Summe").grid(row=5,column=1)
Entry(root,textvariable=summe,validate='key',validatecommand=valiMakeD).grid(row=5,column=2)
#1
Label(root,text="Betrag 1:").grid(row=1,column=1)
Entry(root,textvariable=a,validate='key',validatecommand=valiDa).grid(row=1,column=2)
#2
Label(root,text="Betrag 2:").grid(row=2,column=1)
Entry(root,textvariable=b,validate='key',validatecommand=valiDb).grid(row=2,column=2)
#3
Label(root,text="Betrag 3:").grid(row=3,column=1)
Entry(root,textvariable=c,validate='key',validatecommand=valiDc).grid(row=3,column=2)
#4
Label(root,text="Betrag 4:").grid(row=4,column=1)
Entry(root,textvariable=d,validate='key',validatecommand=valiDd).grid(row=4,column=2)

#reset
Button(root,text="zuruecksetzen",command=reset).grid(row=6,column=1)

#skonto
Label(root,text="Skonto 2%").grid(row=7,column=1)
Entry(root,textvariable=skonto2).grid(row=7,column=2)

Label(root,text="Skonto 3%").grid(row=8,column=1)
Entry(root,textvariable=skonto3).grid(row=8,column=2)



root.mainloop()
