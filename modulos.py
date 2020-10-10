
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

def NoTerminales(dic):
  nonTerminals = []
  for e in dic:
    if e not in nonTerminals:
      nonTerminals.append(e)
  
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
    if(e[0] == '(' or e[0] == '[' or e[0] == '{'):
      terminales.remove(e)
      for i in e:
        terminales.append(i)

  terminales = list(set(terminales))
  for i in no_terminales:
    if (i in terminales):
      terminales.remove(i)
  
  if ('ε' in terminales):
    terminales.remove('ε')

  return terminales

def PrimerosSimples(dic):
  terminales = Terminales(dic)
  no_terminales = NoTerminales(dic)
  todos = list(no_terminales + terminales)
  # print("modulo primeros simple variable todos: ",todos)
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
  
  for e in primeros:
    primeros[e] = set(primeros[e])

  return primeros

def PrimerosNoTerminales(dic):
  no_terminales = NoTerminales(dic)
  solo_primeros = PrimerosSimples(dic)
  answer = {}
  for e in no_terminales:
    answer[e] = set()
  for e in no_terminales:
    # if (len(answer[e]) > 0):
      # continue
    # else:        
    answer[e] = getPrimeros(e,answer,no_terminales,solo_primeros)
  return answer

def getPrimeros(e,ans,no_terminales,prims):  
  for i in prims[e]:
    if (i not in no_terminales):
      ans[e].add(i)
    else:
      ans[e] = ans[e].union(getPrimeros(i,ans,no_terminales,prims))
  return ans[e]

def PrimerosTodos(dic):
  ans = {}
  ans = PrimerosNoTerminales(dic)
  ans.update(PrimerosTerminales(dic))
  return ans

def SplitForFollows(dic):
  dic2 = dic
  for e in dic:
    aux = []
    for token in dic[e]:      
      x = []
      for tok in token:
        for st in tok.split(' '):
          if(len(st) > 1 and (st[0] == "(" or st[0] == "[" or st[0] == '{')):
            for i in st:
              x.append(i)
          else:
            x.append(st)
      aux.append(x)
    dic[e] = aux 
  for _ in dic:
    print(_,dic[_])
  Siguientes(dic,dic2)
  return dic

def Siguientes(dic,dic2): # recibe el diccionario que devuelve SplitForFollows
  primeros = PrimerosTodos(dic2)
  no_terminales = NoTerminales(dic2)
  ans = {}
  for e in dic:
    ans[e] = set()

  ans[no_terminales[0]].add('$')
  # print("este en el ans de siguientes: \n",ans)
  # print("esto es primeros: ",primeros)
  for e in dic:
    pila = []
    ans[e] = getSiguientes(e,dic,ans,primeros,pila)
    # print(ans)
  return ans
              
def getSiguientes(e,dic,ans,primeros,pila):
  if(e in pila):
    print(ans)
    return ans[e]

  pila.append(e)  
  for premisa in dic:
    for regla in dic[premisa]:
      for ind in range(len(regla)):
        if( e == regla[ind]):
          if (ind != (len(regla) -1)):
            for prim in primeros[regla[ind + 1]]:
              if (prim == 'ε' or regla[ind + 1] == 'ε'):
                ans[e] = ans[e].union(getSiguientes(premisa,dic,ans,primeros,pila))
              else:
                ans[e].add(prim)
          else:
            ans[e] = ans[e].union(getSiguientes(premisa,dic,ans,primeros,pila))
  pila.pop()
  print(ans)
  return ans[e]

def getTabla(dic):
  primeros = PrimerosTodos(dic)
  
  reglas_separadas = SplitForFollows(dic)
  siguientes = Siguientes(reglas_separadas,dic)
  terminales = sorted(Terminales(dic))
  terminales.append('$')
  no_terminales = NoTerminales(dic)

  print("primeros: ",primeros)
  print("siguientes: ",siguientes)
  print("terminales: ",terminales)
  print("no_terminales: ",no_terminales)

  M = {}
  for nt in no_terminales:
    M[nt] = {}
    for t in terminales:
      M[nt][t] = set()

  for premisa in dic:
    for regla in dic[premisa]:   
      # print("regla: ",regla)       
      p = regla[0]
      # print("premisa: ",premisa)
      if (p == 'ε'):
        for sig in siguientes[premisa]:
          M[premisa][sig].add(str(premisa) + " -> " + str(' '.join(regla)))
      else:
        for prim in primeros[p]:
          # print("llega aqui",prim)
          if(prim != 'ε'):
            M[premisa][prim].add(str(premisa) + " -> " + str(' '.join(regla)))

  for nt in M:    
    for t in M[nt]:
      if (len(M[nt][t]) == 0):
        M[nt][t].add("error")

  for nt in M:
    print(nt,M[nt])
  
  return M   



