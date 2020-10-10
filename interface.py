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
    self.ventana['bg'] = '#49A'
    self.ventana.geometry('900x730')
    self.texto = ""
    self.traduc = ""
    self.finished = True
    self.copia = ""

    self.display1 = scrolledtext.ScrolledText(self.ventana,width=43,height=10,font=("Cascadia Code",10))
    self.display1.place(x=20,y=65)
    self.display2 = scrolledtext.ScrolledText(self.ventana,width=44,height=10,font=("Cascadia Code",10))
    self.display2.place(x=545,y=65)
    #----
    self.display3 = scrolledtext.ScrolledText(self.ventana,width=18,height=9,font=("Cascadia Code",10))
    self.display3.place(x=52,y=320)
    self.display4 = scrolledtext.ScrolledText(self.ventana,width=42,height=9,font=("Cascadia Code",10))
    self.display4.place(x=210,y=320)
    self.display5 = scrolledtext.ScrolledText(self.ventana,width=40,height=9,font=("Cascadia Code",10))
    self.display5.place(x=580,y=320)
    self.display6 = scrolledtext.ScrolledText(self.ventana,width=115,height=11,font=("Cascadia Code",10))
    self.display6.place(x=55,y=540)
    #----
    #self.display7 = scrolledtext.ScrolledText(self.ventana,width=20,height=30,font=("Cascadia Code",10))
    #self.display7.place(x=900,y=50)
    #self.display8 = scrolledtext.ScrolledText(self.ventana,width=20,height=30,font=("Cascadia Code",10))
    #self.display8.place(x=1062,y=50)
    #self.display9 = scrolledtext.ScrolledText(self.ventana,width=20,height=30,font=("Cascadia Code",10))
    #self.display9.place(x=1224,y=50)
    #---
    
    self.label1 = Label(self.ventana,text="ANALIZADOR", relief="groove", bd = 3,bg="white",font=("Arial Black",14),width=68)
    self.label1.place(x=2,y=0.5)
    self.label1 = Label(self.ventana,text="ENTRADA(reglas)",font=("Open Sans bold",11),width=35)
    self.label1.place(x=20.5,y=38)
    self.label1 = Label(self.ventana,text="SALIDA ",font=("Open Sans bold",11),width=36)
    self.label1.place(x=545.5,y=38)
    #--
    self.label1 = Label(self.ventana,text="Conjuntos Primeros y Siguientes", relief="groove", bd = 3,bg="white", font=("Arial Black",11),width=80)
    self.label1.place(x=3.5,y=260)
    self.label1 = Label(self.ventana,text="Terminales",font=("Open Sans bold",11),width=15)
    self.label1.place(x=54.5,y=292.5)
    self.label1 = Label(self.ventana,text="No Terminales",font=("Open Sans bold",11),width=34)
    self.label1.place(x=212,y=292.5)
    self.label1 = Label(self.ventana,text="Siguientes",font=("Open Sans bold",11),width=33)
    self.label1.place(x=580,y=292.5)
    #--
    self.label1 = Label(self.ventana,text="Tabla de Analisis Sintactico LL", relief="groove", bd = 3, bg="white", font=("Arial Black",11),width=80)
    self.label1.place(x=3,y=475)

    #self.label1 = Label(self.ventana,text="Simbolos No Terminales (NT)", font=("Open Sans bold",8),width=91)
    #self.label1.place(x=55,y=539)
    #self.label1 = Label(self.ventana,text="Simbolos Terminales (T)", font=("Open Sans bold",10),width=101)
    #self.label1.place(x=55,y=569)

    imagen1 = PhotoImage(file="./img/NoTerminales.png")
    self.Fondo = Label(self.ventana, image = imagen1).place(x=22,y=517)
    imagen2 = PhotoImage(file="./img/Terminales.png")
    self.Fondo = Label(self.ventana, image = imagen2).place(x=54,y=510)
    #botones
    
    # self.btnReset = Button(self.ventana, text="Ingresar Texto",font=("Cascadia Code",8),padx=4,pady=1,command=self.copiar)
    # self.btnReset.place(x=20,y=430)


    self.limpiar1=Button(self.ventana, text="Limpiar",bg = 'khaki2', font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar1).place(x=20,y=231)
    self.limpiar2=Button(self.ventana, text="Limpiar",bg = 'khaki2',font=("Cascadia Code",10),padx=4,pady=1,command=self.limpiar2).place(x=817,y=231)
    self.SepararReglas=Button(self.ventana, text="Separar Reglas",bg = 'khaki2',font=("Cascadia Code",10),padx=22,pady=1,command=self.int_sep_reglas).place(x=372,y=50)
    self.VAmbigüedad=Button(self.ventana,   text="Verificar Ambigüedad",bg = 'khaki2',font=("Cascadia Code",10),padx=5,pady=1,command=self.verify_amb).place(x=372,y=80)
    self.CAmbigüedad=Button(self.ventana,   text="Corregir  Ambigüedad",bg = 'khaki2',font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_amb).place(x=372,y=110)
    self.VRecursividad=Button(self.ventana, text="Verificar Recursividad",bg = 'khaki2',font=("Cascadia Code",10),padx=5,pady=1,command=self.verify_rec).place(x=372,y=140)
    self.CRecursividad=Button(self.ventana, text="Corregir  Recursividad",bg = 'khaki2',font=("Cascadia Code",10),padx=4,pady=1,command=self.sol_rec).place(x=372,y=170)
    self.actEntrada=Button(self.ventana, text="  <<<<<  ",bg = 'khaki2',font=("Cascadia Code",10),padx=39,pady=1,command=self.actualizar).place(x=372,y=200)
    #--
    self.ConjPrimeros=Button(self.ventana, text="P\nR\nI\nM\nE\nR\nO\nS",bg = 'khaki2',font=("Cascadia Code",9),padx=4,pady=10,command=self.primeros).place(x=20,y=320)
    self.ConjSiguientes=Button(self.ventana, text="S\nI\nG\nU\nI\nE\nN\nT\nE\nS",bg = 'khaki2',font=("Cascadia Code",8),padx=7,pady=1,command=self.siguientes).place(x=545,y=318)
    self.Recomendaciones=Button(self.ventana, text="( ! )",bg = 'tomato',font=("Arial Black",10),padx=3,pady=1,command=self.recomendaciones).place(x=852,y=3)
    #--
    self.Tablas=Button(self.ventana, text="Construir",font=("Cascadia Code",10), bg = 'khaki2',padx=7,pady=1.5,command=self.Tabla).place(x=22,y=510)


    self.ventana.mainloop()

    # Mensajes
 
    #---------------------------------------------------
  def Tabla(self):
    nr = 8
    nc = 12
    for r in range(nr):  
      for c in range(nc):
        Label(self.display6, text = 'R%s/C%s'%(r,c), font=("Open Sans",10), borderwidth=1).grid(padx = 5, ipadx = 9,row = r,column=c)
    #self.display6.insert(tk.INSERT,rpta)
    
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
    conj_primeros_general = PrimerosSimples(dic1)
    print("conjunto primeros general : ",conj_primeros_general)
    rpta1 = ""
    aux1 = ""
    rpta2 = ""
    aux2 = ""
    # for i in conj_primeros_no_terminales:
    #   conj_primeros_no_terminales[i].sort()    

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
