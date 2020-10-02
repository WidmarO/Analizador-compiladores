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
    self.ventana.geometry('960x650')
    self.texto = ""
    self.traduc = ""
    self.finished = True
    self.copia = ""

    self.display1 = scrolledtext.ScrolledText(self.ventana,width=45,height=15,font=("Cascadia Code",10))
    self.display1.place(x=20,y=70)
    self.display2 = scrolledtext.ScrolledText(self.ventana,width=45,height=15,font=("Cascadia Code",10))
    self.display2.place(x=600,y=70)
    #----
    self.display3 = scrolledtext.ScrolledText(self.ventana,width=45,height=12,font=("Cascadia Code",10))
    self.display3.place(x=100,y=440)
    self.display4 = scrolledtext.ScrolledText(self.ventana,width=45,height=12,font=("Cascadia Code",10))
    self.display4.place(x=520,y=440)
    #---
    self.label1 = Label(self.ventana,text="ANALIZADOR",bg="light steel blue",font=("Cascadia Code",18),width=20)
    self.label1.place(x=350,y=5)
    self.label1 = Label(self.ventana,text="ENTRADA(reglas)",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=120,y=30)
    self.label1 = Label(self.ventana,text="SALIDA",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=700,y=30)
    #--
    self.label1 = Label(self.ventana,text="Conjuntos Primeros y Siguientes",font=("Zeppelin 2",14),width=25)
    self.label1.place(x=350,y=365)
    #--
    
    #botones
    
    # self.btnReset = Button(self.ventana, text="Ingresar Texto",font=("Cascadia Code",8),padx=4,pady=1,command=self.copiar)
    # self.btnReset.place(x=20,y=430)


    self.limpiar1=Button(self.ventana, text="Limpiar",font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar1).place(x=20,y=320)
    self.limpiar2=Button(self.ventana, text="Limpiar",font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar2).place(x=600,y=320)
    self.SepararReglas=Button(self.ventana, text="Separar Reglas",font=("Cascadia Code",10),padx=4,pady=1,command=self.int_sep_reglas).place(x=442,y=120)
    self.VAmbigüedad=Button(self.ventana,   text="Verificar Ambigüedad",font=("Cascadia Code",10),padx=4,pady=1,command=self.verify_amb).place(x=422,y=150)
    self.CAmbigüedad=Button(self.ventana,   text="Corregir  Ambigüedad",font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_amb).place(x=422,y=180)
    self.VRecursividad=Button(self.ventana, text="Verificar Recursividad",font=("Cascadia Code",10),padx=4,pady=1,command=self.verify_rec).place(x=422,y=210)
    self.CRecursividad=Button(self.ventana, text="Corregir  Recursividad",font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_rec).place(x=422,y=240)
    self.actEntrada=Button(self.ventana, text="  <<<<<  ",font=("Cascadia Code",10),padx=4,pady=1,command=self.actualizar).place(x=455,y=270)
    #--
    self.ConjPrimeros=Button(self.ventana, text="Primeros",font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar1).place(x=100,y=400)
    self.ConjSiguientes=Button(self.ventana, text="Siguientes",font=("Cascadia Code",10),padx=7,pady=1,command=self.limpiar2).place(x=770,y=400)
    #--
    self.ventana.mainloop()


  def actualizar(self):
    self.saveText = self.display2.get('1.0', tk.END)
    self.display1.delete('1.0',END)
    self.display1.insert(tk.INSERT, self.saveText)

  def copiar(self):
    self.saveText = self.display1.get('1.0', tk.END)
    # aux = [self.saveText]
    print(self.saveText)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,self.saveText)

  def limpiar1(self):
    self.display1.delete('1.0',END)

  def limpiar2(self):
    self.display2.delete('1.0',END)
  def leer(self):
    self.saveText = self.display1.get('1.0', tk.END)
    datos = str(self.saveText)
    reglas = LeerDatos(datos)
    return reglas

  def int_sep_reglas(self):
    self.saveText = self.display1.get('1.0', tk.END)
    reglas = self.leer()
    rpta = SepararReglas(reglas)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,rpta)

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
  
  def sol_rec(self):
    self.saveText = self.display1.get('1.0', tk.END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    # err = AnalizarForRec(dic1)
    dic2 = CorregirRec(dic1)
    rpta = MostrarCorregido(dic2)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,rpta)

  def verify_amb(self):
    self.saveText = self.display1.get('1.0', END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    err = AnalizarForAmb(dic1)
    if (len(err) == 0):
      print("no hay Ambiguedad")
      rpta = "no hay Ambiguedad"
      self.display2.delete('1.0',END)
      self.display2.insert(tk.INSERT,rpta)
    else:
      print("si hay Ambiguedad")
      rpta = "si hay Ambiguedad"
      self.display2.delete('1.0',END)
      self.display2.insert(tk.INSERT,rpta)
  
  def sol_amb(self):
    self.saveText = self.display1.get('1.0', END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    # err = AnalizarForAmb(dic1)
    dic2 = CorregirAmb(dic1)
    rpta = MostrarCorregido(dic2)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,rpta)



if __name__=="__main__":
  Analizador()