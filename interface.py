from tkinter import *
from tkinter import scrolledtext
from tkinter import font
import tkinter as tk
from tkinter import messagebox

from modulos import *

class Analizador():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("COMPILADORES")
    #self.label1 = Label(self.ventana,text="Entrada(reglas)",font=("Zeppelin 2",14),bg="light steel blue",width=64)
    self.ventana['bg'] = 'light steel blue'
    self.ventana.geometry('1050x680')
    self.texto = ""
    self.traduc = ""
    self.finished = True
    self.copia = ""

    self.display1 = scrolledtext.ScrolledText(self.ventana,width=40,height=12,font=("Cascadia Code",12))
    self.display1.place(x=20,y=70)
    self.display2 = scrolledtext.ScrolledText(self.ventana,width=40,height=12,font=("Cascadia Code",12))
    self.display2.place(x=620,y=70)
    #----
    self.display3 = scrolledtext.ScrolledText(self.ventana,width=18,height=12,font=("Cascadia Code",12))
    self.display3.place(x=20,y=440)
    self.display4 = scrolledtext.ScrolledText(self.ventana,width=34,height=12,font=("Cascadia Code",12))
    self.display4.place(x=230,y=440)
    self.display5 = scrolledtext.ScrolledText(self.ventana,width=40,height=12,font=("Cascadia Code",12))
    self.display5.place(x=600,y=440)
    #---
    self.label1 = Label(self.ventana,text="ANALIZADOR",bg="light steel blue",font=("Cascadia Code",18),width=20)
    self.label1.place(x=370,y=5)
    self.label1 = Label(self.ventana,text="ENTRADA(reglas)",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=120,y=30)
    self.label1 = Label(self.ventana,text="SALIDA",font=("Zeppelin 2",14),width=15)
    self.label1.place(x=715,y=30)
    #--
    self.label1 = Label(self.ventana,text="Conjuntos Primeros y Siguientes",font=("Zeppelin 2",16),width=25)
    self.label1.place(x=350,y=335)
    self.label1 = Label(self.ventana,text="Terminales",font=("Zeppelin 2",10),width=15)
    self.label1.place(x=40,y=410)
    self.label1 = Label(self.ventana,text="No Terminales",font=("Zeppelin 2",10),width=15)
    self.label1.place(x=330,y=410)
    #--
    
    #botones
    
    # self.btnReset = Button(self.ventana, text="Ingresar Texto",font=("Cascadia Code",8),padx=4,pady=1,command=self.copiar)
    # self.btnReset.place(x=20,y=430)


    self.limpiar1=Button(self.ventana, text="Limpiar",font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar1).place(x=20,y=310)
    self.limpiar2=Button(self.ventana, text="Limpiar",font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar2).place(x=970,y=310)
    self.SepararReglas=Button(self.ventana, text="Separar Reglas",font=("Cascadia Code",10),padx=4,pady=1,command=self.int_sep_reglas).place(x=472,y=120)
    self.VAmbigüedad=Button(self.ventana,   text="Verificar Ambigüedad",font=("Cascadia Code",10),padx=4,pady=1,command=self.verify_amb).place(x=452,y=150)
    self.CAmbigüedad=Button(self.ventana,   text="Corregir  Ambigüedad",font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_amb).place(x=452,y=180)
    self.VRecursividad=Button(self.ventana, text="Verificar Recursividad",font=("Cascadia Code",10),padx=4,pady=1,command=self.verify_rec).place(x=452,y=210)
    self.CRecursividad=Button(self.ventana, text="Corregir  Recursividad",font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_rec).place(x=452,y=240)
    self.actEntrada=Button(self.ventana, text="  <<<<<  ",font=("Cascadia Code",10),padx=4,pady=1,command=self.actualizar).place(x=485,y=270)
    #--
    self.ConjPrimeros=Button(self.ventana, text="Primeros",font=("Cascadia Code",10),padx=4,pady=1,command=self.primeros).place(x=220,y=375)
    self.ConjSiguientes=Button(self.ventana, text="Siguientes",font=("Cascadia Code",10),padx=7,pady=1,command=self.siguientes).place(x=735,y=390)
    self.Recomendaciones=Button(self.ventana, text="Ayuda",font=("Cascadia Code",10),padx=3,pady=1,command=self.recomendaciones).place(x=1,y=1)
    #--
    self.ventana.mainloop()

    # Mensajes
 
    #---------------------------------------------------
  def recomendaciones(self):
    messagebox.showinfo(message="NOTA: Si deseas ingresar varias reglas en una sola linea, debes separarlas con el siguiente caracter:\n\t        ' | '\nEjm: \n\tE -> + A | - A | B \n\n"
    "Para ingresar las reglas debe seguir el siguiente formato: \n\n\t E -> a b E \n\nDonde cada estado debe estar separado por un espacio.", title="Recomendaciones")
  
  def actualizar(self):
    self.saveText = self.display2.get('1.0', tk.END)
    self.display1.delete('1.0',END)
    self.display1.insert(tk.INSERT, self.saveText)

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
    # self.saveText = self.display1.get('1.0', tk.END)
    reglas = self.leer()
    rpta = SepararReglas(reglas)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,rpta)

  def verify_rec(self):
    # self.saveText = self.display1.get('1.0', tk.END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    err = AnalizarForRec(dic1)
    if (len(err) == 0):
      # Mensaje = 
      messagebox.showinfo(message="No existe recursividad", title="Recursividad")
      #self.display2.delete('1.0',END)
      # self.ventana.insert(tk.INSERT,Mensaje)
    else:
      Mensaje = messagebox.showinfo(message="Si existe recursividad", title="Recursividad")
      Pregunta = messagebox.askyesno(message="¿Corregir recursividad?", title="Recursividad")
      print(Pregunta)
      if (Pregunta):
        self.sol_rec()
      #self.display2.delete('1.0',END)
      # self.ventana.insert(tk.INSERT,Mensaje)
  
  def sol_rec(self):
    # self.saveText = self.display1.get('1.0', tk.END)
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
      messagebox.showinfo(message="No existe ambiguedad", title="Ambiguedad")

    else:
      messagebox.showinfo(message="Si existe ambiguedad", title="Ambiguedad")
      Pregunta = messagebox.askyesno(message="¿Corregir ambiguedad?", title="Ambiguedad")
      print(Pregunta)
      if (Pregunta):
        self.sol_amb()
      # self.ventana.insert(tk.INSERT,Mensaje)
  
  def sol_amb(self):
    # self.saveText = self.display1.get('1.0', END)
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    # err = AnalizarForAmb(dic1)
    dic2 = CorregirAmb(dic1)
    rpta = MostrarCorregido(dic2)
    self.display2.delete('1.0',END)
    self.display2.insert(tk.INSERT,rpta)

  def primeros(self):
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    conj_primeros_terminales = PrimerosTerminales(dic1)
    conj_primeros_no_terminales = PrimerosNoTerminales(dic1)

    rpta1 = ""
    aux1 = ""
    rpta2 = ""
    aux2 = ""
    for i in conj_primeros_no_terminales:
      conj_primeros_no_terminales[i].sort()    

    for i in conj_primeros_no_terminales:
      aux1 += "First ( "+str(i)+" )" + " = { " + str(conj_primeros_no_terminales[i])[1:-1] + "} " + "\n"
    rpta1 = str(aux1)

    for i in conj_primeros_terminales:
      aux2 += "First ( "+str(i)+" )" + " = { " + str(conj_primeros_terminales[i])[1:-1] + "} " + "\n"
    rpta2 = str(aux2)

    self.display4.delete('1.0',END)
    self.display4.insert(tk.INSERT,rpta1)

    self.display3.delete('1.0',END)
    self.display3.insert(tk.INSERT,rpta2)

    
    print("No terminales: ",NoTerminales(dic1))
    print("terminales:",Terminales(dic1))

  def siguientes(self):
    reglas = self.leer()
    dic1 = OrganizarToAnalisis(reglas)
    dic2 = SplitForFollows(dic1)

    chr = ""
    for i in dic2:
      chr += str(i) + " = " + str(dic2[i]) + "\n"

    self.display5.delete('1.0',END)
    self.display5.insert(tk.INSERT,chr)

if __name__=="__main__":
  Analizador()