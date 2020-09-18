# **<center>ANALIZADOR</center>**

---

El propósito de este trabajo es crear un programa que elimine la ambigüedad y recursión de una gramática, asi mismo determine los conjuntos primeros y siguientes.

### Ejemplos...

Dado el siguiente conjunto de reglas determinar si tienen problemas de ambiguedad o recursividad, si es el caso corregirlos.

```py
# Conjunto de reglas
S -> Var := E
E -> E + E | E + (E) | (E)
E -> E - T
E -> Var | Num
Var -> a | b | c | d | e
Num -> 0 | 1 | 2 | 3 | 9
# Tiene Recursividad y Ambiguedad
# Corregimos Recursividad
S -> Var := E
E -> (E) E' | Var E' | Num E'
E' -> + E E' | + (E) E' | - T E' | ε
Var -> a | b | c | d | e
Num -> 0 | 1 | 2 | 3 | 9
# Aun tiene problemas de Ambiguedad
# corregimos ambiguedad
S -> Var := E
E -> (E) E' | Var E' | Num E'
E' -> + E'' | - T E' | ε
E'' -> E E' | (E) E'
Var -> a | b | c | d | e
Num -> 0 | 1 | 2 | 3 | 9
# Ahora nuestras reglas no tienen problemas de ambiguedad ni recursividad :)
```

### Empezamos... 🚀

_Para un mayor entendimiento del programa realizamos un diagrama de flujo, el cual muestra una secuencia de pasos que componen el proceso del programa que tienen una conexión entre sí._

###### <center>DIAGRAMA DE FLUJO</center>

![diagrama.png](https://raw.githubusercontent.com/WidmarO/Analizador-compiladores/master/img/diagrama.png)

### Construido con... 🛠️

- Lenguaje: [Python 3.6.9](https://www.python.org/)
- Servicio Cloud: [Google Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb)
- Servicio Local: [Jupyter-Notebook](https://jupyter.org/)
- Diagrama de flujo: [Visual Paradigm](https://www.visual-paradigm.com/)
- Interfaz Grafica: [tkinter](https://docs.python.org/2/library/tkinter.html)
- Editor: [Visual Studio Code](https://code.visualstudio.com/)

## Codificacion del programa 📄

La codificacion del programa fue dividido en lo siguiente:

#### Nota:

Al ingresar las reglas, debe separar por espacio los estados y por " | " (una barra vertical) en caso de colocar mas reglas en una sola linea.

### Codigo que resuelve la recursion ⌨️

```py
def CorregirRec(dic):

  err = AnalizarForRec(dic)
  corregido = {}
  for e in dic:
    if e in err:
      corregido[e] = []
      corregido[e + "'"] = []
      for token in dic[e]:
        if (len(token) == 1):
          corregido[e].append([token[0] + " " + e + "'"])
        else:
          corregido[e + "'"].append([(token[1]) + " " + e + "'"])
      corregido[e + "'"].append(["\u03B5"])
    else:
      corregido[e] = dic[e]
  return corregido
```

### Codigo que resuelve la ambigüedad ⌨️

```py
def CorregirUnaAmb(dic):
  err = AnalizarForAmb(dic)
  corregido = {}
  for e in dic:
    # print("esete es el e: ",e)
    if e in err:
      # print("entro en e.values", e)
      corregido[e] = []
      corregido[e + "'"] = []
      corregido[e].append([err[e] + " " + e + "'"])
      for token in dic[e]:
        if (token[0] != err[e]):
          corregido[e].append(token)
        else:
          corregido[e + "'"].append([token[1]])
    else:
      corregido[e] = dic[e]
  return corregido
```

## Despliegue 📦

_No requiere nada mas que python 3.^ para poder correr el programa,solo ejecute el archivo interface.py con python, la libreria tkinter viene integrada en python, los archivos de extension .ipynb pueden abrirse con Google Colab_.

## Wiki 📖

No tenemos un wiki :( ... pero puedes ver mas sobre el proyecto en el archivo .ipynb, puedes acceder haciendo click aqui [Wiki](https://colab.research.google.com/drive/1n1UBUUUta2xj2JdlEJcHtiOpa_qsZsAp?usp=sharing).

## Versionado 📌

Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/WidmarO/Analizador-compiladores/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Widmar Raul** - _Trabajo Inicial_ - [WidmarO](https://github.com/WidmarO)
- **Melanie Indira** - _Trabajo Inicial_ - [Melanie279](https://github.com/Melanie279)
- **Nadiabeth Diana** - _Trabajo Inicial_ - [Nadiabeth15](https://github.com/Nadiabeth15)

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢.
- Agradecemos a todas las personas involucradas (nosotros) 🤓.
- Esperamos les sea util, gracias por descargar.

---

⌨️ con ❤️ por [WidmarO](https://github.com/WidmarO) 😊
