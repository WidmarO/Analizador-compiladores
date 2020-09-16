from tkinter import *
from tkinter import scrolledtext
from tkinter import font

from test import *

def main():
  #...........creando ventana
  ventana= Tk()
  ventana.title("COMPILADORES")
  ventana.geometry('730x500')
  ventana.configure(background='light steel blue')

  #...........etiquetas
  #bg="red"...subrayado
  #fg=Color letra
  #font= fuente de letra
  titulo=Label(ventana,text="ANALIZADOR" ,font=("Karate",16),bg="light steel blue",fg="black").place(x=308,y=5)


  #............crear espacio de texto para las reglas
  ingresarReglas=Label(ventana,text="Ingresar Reglas:" ,font=("Zeppelin 2",14),bg="light steel blue",fg="black").place(x=20,y=25)
  espacioReglas = scrolledtext.ScrolledText(ventana,width=30,height=10).place(x=10,y=50)


  #............botones
  separar=Button(ventana, text="Separar Reglas",font=("Verdana",8),padx=4,pady=1).place(x=20,y=220)
  limpiar=Button(ventana, text="Limpiar",font=("Verdana",8),padx=4,pady=1).place(x=200,y=220)
  VAmbigüedad=Button(ventana, text="Verificar Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=300,y=75)
  CAmbigüedad=Button(ventana, text="Corregir Ambigüedad",font=("Verdana",8),padx=4,pady=1).place(x=300,y=105)
  VRecursividad=Button(ventana, text="Verificar Recursividad",font=("Verdana",8),padx=4,pady=1).place(x=300,y=135)
  CRecursividad=Button(ventana, text="Corregir Recursividad",font=("Verdana",8),padx=4,pady=1).place(x=300,y=165)


  #............crear espacio de reglas sobreescritas
  NuevasReglas=Label(ventana,text="Reglas Reescritas" ,font=("Zeppelin 2",14),bg="light steel blue",fg="black").place(x=530,y=25)
  espacioNuevasReglas = scrolledtext.ScrolledText(ventana,width=30,height=10).place(x=460,y=50)

  #...........hallando conjunto primeros y siguiente............
  conjuntos=Label(ventana,text="Conjunto de Primeros y Siguientes" , font=("Zeppelin 2",15),bg="light steel blue",fg="black").place(x=255,y=250)
  Primeros=Button(ventana, text="Generar Primeros",padx=4,pady=1).place(x=80,y=280)
  Siguientes=Button(ventana, text="Generar Siguientes",padx=4,pady=1).place(x=535,y=280)
  espacioPrimeros = scrolledtext.ScrolledText(ventana,width=30,height=10).place(x=80,y=310)
  espacioSiguientes = scrolledtext.ScrolledText(ventana,width=30,height=10).place(x=390,y=310)

  ventana.mainloop()

main()