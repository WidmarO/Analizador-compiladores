def main():
  # leyendo los datos
  reglas = LeerDatos()
  # Separar Reglas para mostrar
  to_show_rules = SepararReglas(reglas)
  # # Organizar estructura para analizar
  diccionario1 = OrganizarToAnalisis(reglas)
  print('\n======== listo para analisis ==========\n')  
  MostrarCorregido(diccionario1)
  # for _ in diccionario1:
  #   print(_,diccionario1[_])
  print('\n======== corregir recursividad official ==========\n')
  diccionario2 = CorregirRec(diccionario1)
  MostrarCorregido(diccionario2)
  # for i in diccionario2:
  #   print(i,diccionario2[i])
  print('\n======== corregir ambiguedad official ==========\n')
  diccionario3 = CorregirAmb(diccionario1)
  MostrarCorregido(diccionario3)
  # for i in diccionario3:
    # print(i,diccionario3[i])

def LeerDatos(entrada):
  reglas = entrada.split("\n")
  reglas = [item for item in reglas if item]
  for i in range(len(reglas)):
    while(reglas[i][len(reglas[i])-1] == ' '):
      reglas[i] = reglas[i][:-1]
    # print("modulo LeerDatos en modulos.py\n",reglas)
  return reglas

def SepararReglas(reglas):
  rpta = ""
  # newReglas = []
  for regla in reglas:
    aux = regla.split(' -> ',1)
    premisa = aux[0]
    a = aux[1].split(" | ")   
    for tok in a:   
      # newReglas.append(premisa + " -> " + tok)
      rpta += premisa + " -> " + tok + "\n"
  return rpta

def OrganizarToAnalisis(reglas):
  dic = {}
  for row in reglas:
    aux = row.split(" -> ",1)
    premisa = aux[0]
    dic[premisa] = []

  for row in reglas:
    aux = row.split(" -> ",1) 
    premisa = aux[0]
    derecha = aux[1]
    arreglo = derecha.split(" | ")
    for token in arreglo:      
      aux = token.split(' ',1)
      dic[premisa].append(aux)
  return dic

def Reorganizar(dic):
  for e in dic:
    for i in range(len(dic[e])):
      if (len(dic[e][i]) == 1):
        dic[e][i] = dic[e][i][0].split(' ',1)
  return dic

def AnalizarForRec(dic):
  errores = []
  for e in dic:
    for token in dic[e]:
      if (token[0] == e):
        # print("Existe Recursividad")
        errores.append(e)
  errores = list(set(errores))

  if (len(errores) > 0):
    return errores
  else:
    # print("No hay problemas de Recursividad")
    return errores
  
def AnalizarForAmb(dic):
  errores = {}
  aux = {}
  for e in dic:
    aux[e] = {}
    for token in dic[e]:
      aux[e][token[0]] = 0

  for e in dic:
    mayor = 0
    letra = ""
    for token in dic[e]:
      aux[e][token[0]] += 1
      if (aux[e][token[0]] > mayor and aux[e][token[0]] > 1):
        mayor = aux[e][token[0]]
        letra = token[0]

    if (letra != ""):
      errores[e] = letra

  if (len(errores) > 0):
    # print("Existe Ambiguedad en " + e)
    print(errores)
    return errores
  else:
    # print("No hay problemas de Ambiguedad")
    return errores

def CorregirRec(dic):

  err = AnalizarForRec(dic)
  corregido = {}
  for e in dic:
    if e in err:
      corregido[e] = []
      corregido[e + "'"] = []
      for token in dic[e]:
        if (e != token[0]):
          corregido[e].append([token[0] + " " + e + "'"])
        else:
          corregido[e + "'"].append([(token[1]) + " " + e + "'"])
      corregido[e + "'"].append(["ε"])
    else:
      corregido[e] = dic[e]  
  print(corregido)
  return corregido

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
        if (token[0] == err[e] and len(token) == 1):
          continue

        if (token[0] != err[e]):
          corregido[e].append(token)
        else:
          if (len(token) == 1):
            corregido[e + "'"].append(token)
          else:
            corregido[e + "'"].append([token[1]])      
    else:
      corregido[e] = dic[e]  
  return corregido

def CorregirAmb(dic):
  err = AnalizarForAmb(dic)
  dic3 = dic
  while(len(err) != 0):
    err = AnalizarForAmb(dic3)
    dic3 = CorregirUnaAmb(dic3)
    dic3 = Reorganizar(dic3)
  print(dic3)
  return dic3

def MostrarCorregido(dic):
  rpta = ""
  for premisa in dic:
    chrs = premisa + " -> "
    for regla in dic[premisa]:
      aux = " ".join(regla)
      chrs += aux + ' | '
    chrs = chrs[:-2] + "\n"
    rpta += chrs
  return rpta

def NoTerminales(reglas):
  nonTerminals = set()
  for i in reglas:
    aux = i.split(" -> ")
    nonTerminals.add(aux[0])
  nonTerminals = list(nonTerminals)
  return nonTerminals

def Terminales(dic):
  no_terminales = NoTerminales(dic)
  terminales = []
  for e in dic:
    for token in dic[e]:
      for est in token:
        for x in est.split(' '):          
          terminales.append(x)
  
  for e in terminales:
    if(e[0] == '(' or e[0] == '['):
      terminales.remove(e)
      for i in e:
        terminales.append(i)

  terminales = list(set(terminales))
  for i in no_terminales:
    if (i in terminales):
      terminales.remove(i)

  return terminales

def PrimerosSimples(dic):
  terminales = Terminales(dic)
  no_terminales = NoTerminales(dic)
  todos = set(terminales + no_terminales)
  conj_primeros = {}

  for e in todos:
    conj_primeros[e] = set()

  for i in terminales:
    if(i == "ε"):
      continue
    else:
      conj_primeros[i].add(i)

  for e in dic:
    for token in dic[e]:
      if (len(token[0]) > 1 and (token[0][0] == "(" or token[0][0] == "[")):
        conj_primeros[e].add(token[0][0])
      else:
        conj_primeros[e].add(token[0])      

  for e in conj_primeros:
    conj_primeros[e] = list(conj_primeros[e])

  return conj_primeros

def PrimerosTerminales(dic):
  terminales = Terminales(dic)
  primeros = PrimerosSimples(dic)
  aux = []
  for e in primeros:
    if (e not in terminales):
      aux.append(e)

  for x in aux:
    del primeros[x]

  return primeros

def PrimerosNoTerminales(dic):
  no_terminales = NoTerminales(dic)
  primeros = PrimerosSimples(dic)
  ans = primeros

  aux = []
  for e in primeros:
    if (e not in no_terminales):
      aux.append(e)
  
  for x in aux:
    del primeros[x]
  
  for e in primeros:
    for est in primeros[e]:
      if(est in primeros):
        ans[e].remove(est)
        for i in primeros[est]:
          ans[e].append(i)

  return ans


def Primeros1(dic):
  conj_primeros = {}
  terminales = Terminales(dic)
  no_terminales = NoTerminales(dic)
  todos = set(terminales + no_terminales)
  
  for i in todos:
    conj_primeros[i] = set()
  # primeros para los terminales
  for i in terminales:
    # if(i == "")
    conj_primeros[i].add(i)
  # primeros de los no terminales
  for e in dic:
    for token in dic[e]:
      if(token[0] in terminales):
          conj_primeros[e].add(token[0])        

      if(len(token[0]) > 1 and (token[0][0] == '(' or token[0][0] == '(')):
        conj_primeros[e].add(token[0][0])
      
      # if(token[0] is in no_terminales):

  
  # for i in no_terminales:10

  return conj_primeros

# main()


