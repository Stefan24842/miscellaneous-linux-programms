from Tkinter import *
from tkFileDialog import *
from PIL import Image
import os

def browse():
      path.set(askopenfilename(filetypes=[("Bilder", ".jpg"), ("Bilder", ".JPG"), ("Bilder", ".png"), ("Bilder", ".PNG"), ("Alles","*.*")]))

root = Tk()
root.wm_title("Bild umwandeln")
imgtp = StringVar()
imgtp.set(".jpg")
path=StringVar()

#Source
Label(root,text="Quell-Datei:").grid(row=1,column=1)
Button(root,text="Durchsuchen",command=browse).grid(row=2,column=1)
Entry(root,textvariable=path).grid(row=3,column=1)
#Dateityp
Label(root, text="Ziel-Dateityp:", justify = LEFT).grid(row=1,column=2)
Radiobutton(root, 
            text="JPG (.jpg)", 
            variable=imgtp, 
            value=".jpg").grid(row=2,column=2)
Radiobutton(root, 
            text="PDF (.pdf)",
            variable=imgtp, 
            value=".pdf"
            ).grid(row=3,column=2)
#Size:
Label(root,text="Groesse:").grid(row=4,column=1)
sWid=Scale(root, from_=1,to=100,orient=HORIZONTAL)
sWid.set(33)
sWid.grid(row=5,column=1)
#Quality
Label(root,text="Qualitaet:").grid(row=4,column=2)
qWid=Scale(root, from_=1,to=100,orient=HORIZONTAL)
qWid.set(33)
qWid.grid(row=5,column=2)


def start():
      im=Image.open(path.get())
      newSize=im.size[0]/100.0*sWid.get()
      command= "convert "+"'"+path.get()+"'"+" -resize "+str(newSize)+" -quality "+str(qWid.get())+" "+"'"+path.get()[0:len(path.get())-4]+"_konvertiert"+imgtp.get()+"'"
      os.system(command)
      print command

Button(root, text="Beenden",command=root.destroy).grid(row=6,column=1)
Button(root, text="Start",command=start).grid(row=6,column=2)


root.mainloop()
