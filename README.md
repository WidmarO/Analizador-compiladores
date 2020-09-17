# **<center>ANALIZADOR</center>**

---

El propósito de este trabajo es crear un programa que elimine la ambigüedad y recursión de una gramática, asi mismo determine los conjuntos primeros y siguientes.

### Empezamos... 🚀

_Para un mayor entendimiento del programa realizamos un diagrama de flujo, el cual muestra una secuencia de pasos que componen el proceso del programa que tienen una conexión entre sí._

###### <center>DIAGRAMA DE FLUJO</center>

$$ E \rightarrow E + E $$

### Construido con... 🛠️

- Lenguaje: Python 3.6.9
- Google Colaboratory
- Visual Paradigm

## Codificacion del programa 📄

La codificacion del programa fue dividido en lo siguiente:

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

### Codigo que halla el conjunto primero ⌨️

```
codigo....
```

### Codigo que halla el conjunto siguiente ⌨️

```
codigo....
```

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
- [Maven](https://maven.apache.org/) - Manejador de dependencias
- [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Widmar Raul** - _Trabajo Inicial_ - [WidmarO](https://github.com/WidmarO)[Melanie279](https://github.com/Melanie279)
- **Melanie Indira** - _Trabajo Inicial_ - [Melanie279](https://github.com/Melanie279)
- **Nadiabeth Diana** - _Trabajo Inicial_ - [Nadiabeth15](https://github.com/Nadiabeth15)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto.

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.

---

⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
`