from tkinter import *
from tkinter.ttk import *
import tkinter
from googletrans import Translator

#Deficion de funciones
def Borrar():
    entr.delete("0","end")
    entr1.delete("0","end")

def Traducir():
    inn=entrada.get()
    if inn!="":
        if (combo.get())== "Español" and (combo1.get())=="Ingles":
            out=Translator().translate(inn, dest="en")
            salida.set(out.text)

        elif(combo.get())== "Inglés" and (combo1.get())=="Español":
            out=Translator().translate(inn, dest="es")
            salida.set(out.text)
        
#Colocacion de los lenguajes
languages=["Spanish","English"]


#Diseño de la aplicacion (Interfaz)
ve=Tk()
ve.geometry("700x440")
ve.title("TRADUCTOR DE IDIOMAS")
ve.config(relief="ridge",bd="8",bg="brown")

#Declaracion de string
entrada=StringVar()
salida=StringVar()
languages=StringVar()

#listas desplegables
combo=Combobox(ve,values=["Ingles","Español"])
combo.place(x=80,y=60)
combo.current(1)
combo1=Combobox(ve,values=["Ingles","Español"])
combo1.place(x=450,y=60)
combo1.current(0)

entr=tkinter.Entry(justify=tkinter.LEFT,textvariable=entrada,font=("Verdana",12))
entr.place(x=20,y=150,height=200,width=250)
entr1=tkinter.Entry(justify=tkinter.LEFT,textvariable=salida,font=("Verdana",12))
entr1.place(x=400,y=150,height=200,width=250)

#botones
bo=Button(ve,text="BORRAR",command=Borrar).place(x=300,y=250)
trad=Button(ve,text="TRADUCIR",command=Traducir).place(x=300,y=200)

ve.mainloop()