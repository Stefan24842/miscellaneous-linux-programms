from Tkinter import *
from tkFileDialog import *
import os

def open1():
      path1.set(askopenfilename(filetypes=[("Alles","*.*"), ("PDF", ".pdf")]))
def open2():
      path2.set(askopenfilename(filetypes=[("Alles","*.*"), ("PDF", ".pdf")]))
##def open3():
##      path3.set(askopenfilename(filetypes=[("PDF", ".pdf"), ("Alles","*.*")]))
##def open4():
##      path4.set(askopenfilename(filetypes=[("PDF", ".pdf"), ("Alles","*.*")]))
def save():
      pathe.set(asksaveasfilename(filetypes=[("PDF", ".pdf"), ("Alles","*.*")]))


root = Tk()
root.wm_title("PDFs zusammenfuegen")
imgtp = StringVar()
imgtp.set(".jpg")
path1=StringVar()
path2=StringVar()
##path3=StringVar()
##path4=StringVar()
pathe=StringVar()

#Source
Label(root,text="Einzelne PDF Dateien:").grid(row=1,column=1)
Button(root,text="Durchsuchen",command=open1).grid(row=2,column=2)
Entry(root,textvariable=path1).grid(row=2,column=1)
Button(root,text="Durchsuchen",command=open2).grid(row=3,column=2)
Entry(root,textvariable=path2).grid(row=3,column=1)
##Button(root,text="Durchsuchen",command=open3).grid(row=4,column=2)
##Entry(root,textvariable=path3).grid(row=4,column=1)
##Button(root,text="Durchsuchen",command=open4).grid(row=5,column=2)
##Entry(root,textvariable=path4).grid(row=5,column=1)
#Save as
Label(root,text="Speichern unter:").grid(row=6,column=1)
Button(root,text="Durchsuchen",command=save).grid(row=7,column=2)
Entry(root,textvariable=pathe).grid(row=7,column=1)

def start():
      command= "pdftk '"+path1.get()+"' '"+path2.get()+"' output '"+pathe.get()+"'"
      os.system(command)
      print command

Button(root, text="Beenden",command=root.destroy).grid(row=8,column=1)
Button(root, text="Start",command=start).grid(row=8,column=2)
#Button(root, text="Start",command=start).grid(row=6,column=2)


root.mainloop()
