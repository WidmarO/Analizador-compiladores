from tkinter import *
from tkinter import scrolledtext
from tkinter import font
import tkinter as tk

from modulos import *

class Analizador():
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
    
    self.btnReset = Button(self.ventana, text="Ingresar Texto",font=("Verdana",8),padx=4,pady=1,command=self.copiar)
    self.btnReset.place(x=20,y=430)


    self.limpiar=Button(self.ventana, text="Limpiar",font=("Verdana",8),padx=4,pady=1,command=self.limpiar).place(x=20,y=400)
    self.SepararReglas=Button(self.ventana, text="Separar Reglas",font=("Verdana",8),padx=4,pady=1).place(x=430,y=120)
    self.VAmbigüedad=Button(self.ventana, text="Verificar Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=150)
    self.CAmbigüedad=Button(self.ventana, text="Corregir Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=430,y=180)
    self.VRecursividad=Button(self.ventana, text="Verificar Recursividad",font=("Verdana",8),padx=4,pady=1,command=self.verify_rec).place(x=430,y=210)
    self.CRecursividad=Button(self.ventana, text="Corregir Recursividad",font=("Verdana",8),padx=4,pady=1,command=self.leer).place(x=430,y=240)
    self.ventana.mainloop()



  def copiar(self):
    self.saveText = self.display1.get('1.0', tk.END)
    # aux = [self.saveText]
    print(self.saveText)
    self.display2.insert(tk.INSERT,self.saveText)

  def limpiar(self):
    self.display2.delete('1.0',END)

  def leer(self):
    self.saveText = self.display1.get('1.0', tk.END)
    datos = str(self.saveText)
    reglas = LeerDatos(datos)

    # print(reglas)
    return reglas
  # def organizar(self):
  #   reglas = self.leer()
  #   dic1 = OrganizarToAnalisis()
  # def separar(self):


  def verify_rec(self):
    self.saveText = self.display1.get('1.0', tk.END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    err = AnalizarForRec(dic1)
    if (len(err) == 0):
      print("no hay recursividad")
      rpta = "no hay recursividad"
      self.display2.delete('1.0',END)
      self.display2.insert(tk.INSERT,rpta)
    else:
      print("si hay recursividad")
      rpta = "si hay recursividad"
      self.display2.delete('1.0',END)
      self.display2.insert(tk.INSERT,rpta)


if __name__=="__main__":
  # root = tk.Tk()
  Analizador()