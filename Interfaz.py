from tkinter import *
from tkinter import scrolledtext
from tkinter import font
import tkinter as tk

from test import *

class Analisador():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("COMPILADORES")
    #self.label1 = Label(self.ventana,text="Entrada(reglas)",font=("Zeppelin 2",14),bg="light steel blue",width=64)
    self.ventana['bg'] = 'light steel blue'
    self.ventana.geometry('1000x475')
    self.texto = ""
    self.traduc = ""
    self.finished = True
    self.copia = ""

    self.display1 = scrolledtext.ScrolledText(self.ventana,width=45,height=20)
    self.display1.place(x=20,y=70)
    self.display2 = scrolledtext.ScrolledText(self.ventana,width=45,height=20)
    self.display2.place(x=600,y=70)

    self.label1 = Label(self.ventana,text="ANALIZADOR",bg="light steel blue",font=("Karate",18),width=20)
    self.label1.place(x=350,y=5)
    self.label1 = Label(self.ventana,text="ENTRADA(reglas)",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=150,y=30)
    self.label1 = Label(self.ventana,text="SALIDA",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=720,y=30)
    
    #botones
    
    self.btnReset = Button(self.ventana, text="Ingresar Texto",font=("Verdana",8),padx=4,pady=1,command=self.save)
    self.btnReset.place(x=20,y=430)


    self.limpiar=Button(self.ventana, text="Limpiar",font=("Verdana",8),padx=4,pady=1).place(x=20,y=400)
    self.VAmbigüedad=Button(self.ventana, text="Verificar Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=150)
    self.CAmbigüedad=Button(self.ventana, text="Corregir Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=180)
    self.VRecursividad=Button(self.ventana, text="Verificar Recursividad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=210)
    self.CRecursividad=Button(self.ventana, text="Corregir Recursividad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=240)
    self.ventana.mainloop()

  def save(self):
    self.saveText = self.display1.get('1.0', tk.END)
    print(self.saveText)


if __name__=="__main__":
  # project = Analisador(root)
  Analisador()
  # root.mainloop()
