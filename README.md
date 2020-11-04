# **<center> 💻 ANALIZADOR GRAMATICO (COMPILADORES) 💻 </center>**

---

### Datos Academicos 📖

- **Institucion:** Universidad Nacional de San Antonio Abad del Cusco
- **Facultad:** Facultad de ingenieria electrica, electronica, informatica y mecanica
- **Escuela Prof:** Ingenieria Informatica y de Sistemas

#### Docente:

- **Vanesa Lavilla Alvarez** - _Docente_ - [Concytec](http://directorio.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do;jsessionid=c5a14b2abf78a327623f1a7ccd0f?id_investigador=114602).

#### Trabajo:

- Realizar un analizador gramatico que dado un conjunto de reglas de entrada pueda analizar las reglas, en busca de problemas de recursion o ambiguedad, para luego poder corregirlas y mostrar el resultado.
- Una vez corregidas las reglas obtenemos tambien el conjunto primeros para cada estado, y el conjunto no terminal para estado no terminal.
- Obtenidos ya los conjuntos primeros y siguientes, proseguimos a realiza la tabla DLL.

#### Autores:✒️

- **Widmar Raul Quispe Leon** - _GitHub Account_ - [WidmarO](https://github.com/WidmarO)
- **Melanie Indira Sullca Peralta** - _GitHub Account_ - [Melanie279](https://github.com/Melanie279)
- **Nadiabeth Diana Mallqui Apaza** - _GitHub Account_ - [Nadiabeth15](https://github.com/Nadiabeth15)

---

NOTA: Diculpe las faltas ortograficas tales como tildes, dieresis y demas faltas encontradas a lo largo del cuaderno, esto se debe a que se uso unicamente una distribucion de teclado en ingles para escribir el presente el cual no tiene acceso a dichos caracteres.

## Empezamos... 🚀

Para un mayor entendimiento del programa realizamos un diagrama de flujo, el cual muestra una secuencia de pasos que componen el proceso del programa.

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
# Procedemos a encontrar los conjuntos primeros y siguientes
First ( b ) = { 'b'}
First ( 3 ) = { '3'}
First ( 2 ) = { '2'}
First ( T ) = { 'T'}
First ( e ) = { 'e'}
First ( 1 ) = { '1'}
First ( + ) = { '+'}
First ( c ) = { 'c'}
First ( ) ) = { ')'}
First ( S ) = { 'b', 'e', 'd', 'a', 'c'}
First ( E ) = { 'b', '9', '1', '3', 'd', '0', '2', '(', 'c', 'e', 'a'}
First ( E' ) = { '+', 'ε', '-'}
First ( E'' ) = { 'b', '9', '1', '3', 'd', '0', '2', '(', 'c', 'e', 'a'}
First ( Var ) = { 'b', 'd', 'c', 'e', 'a'}
First ( Num ) = { '9', '1', '3', '0', '2'}
# Obtenidos los conjuntos primeros y siguientes procedemos a construir nuestra tabla.
```

![tabla.png](https://raw.githubusercontent.com/WidmarO/Analizador-compiladores/master/img/tabla.png)

### Construido con... 🛠️

- Lenguaje: [Python 3.6.9](https://www.python.org/)
- Servicio Cloud: [Google Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb)
- Servicio Local: [Jupyter-Notebook](https://jupyter.org/)
- Diagrama de flujo: [Visual Paradigm](https://www.visual-paradigm.com/)
- Interfaz Grafica: [tkinter](https://docs.python.org/2/library/tkinter.html)
- Editor: [Visual Studio Code](https://code.visualstudio.com/)

## Codificacion del programa 📄

A continuacion mostramos los modulos mas importantes del programa...

### Modulo que recibe los datos

Ingresadas las reglas el modulo LeerDatos recibe como parametro las reglas en un string separadas las lineas por "\n" y devuelve un arreglo con las reglas separadas por lineas.

#### Nota:

Al ingresar las reglas, debe separar por espacio los estados y por " | " (una barra vertical) en caso de colocar mas reglas en una sola linea.

## Despliegue 📦

_No requiere nada mas que python 3.^ para poder correr el programa,solo ejecute el archivo interface.py con python, la libreria tkinter viene integrada en python, los archivos de extension .ipynb pueden abrirse con Google Colab_.

## Wiki 📖

No tenemos un wiki :( ... pero puedes ver mas sobre el proyecto en el archivo .ipynb, puedes acceder haciendo click [aqui Wiki](https://colab.research.google.com/drive/1pC42W8I2eGt8ZEss9sjWhpHDtlFpy_k9#scrollTo=HDsNV972EYdX).

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
