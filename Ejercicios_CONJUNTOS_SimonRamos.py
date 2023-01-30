# Lectura de los conjuntos
def elementos(n):
  A = []
  if n == 0:
    return A
  else:
    x = int(input("Digite un número: "))
    A.append(x)
    while n > 1:
      i = int(input("Digite un número: "))
      A = repetido(A,i)
      n -= 1
    return A

def repetido(A,x):
  for i in range(len(A)):
    if A[i] == x:
      x = int(input("Los números no pueden repetirse intente de nuevo: "))
      return repetido(A,x)
  A.append(x)
  return A

# Operaciones generales
def concatena(A,B):
    return A+B

def max (A,n):
  x = A[n-1]
  indice = n-1
  for i in range(n-1,-1,-1):
    if A[i] > x:
      x = A[i]
      indice = i
  return indice

def ordena(A,n):
  while n>1:
    x = A[max(A,n)]
    A[max(A,n)] = A[n-1]
    A[n-1] = x
    n -= 1
  return A

# Unión
def elimina_iguales(A):
  C = []
  for i in range(len(A)-1):
      if A[i] != A[i+1]:
        C.append(A[i])
  C.append(A[len(A)-1])
  return C

# Intersección de los conjuntos

def repetidos(A):
  C = []
  for i in range(len(A)-1):
    if A[i] == A[i+1]:
        C.append(A[i])
  return C

# Diferencia y diferencia simétrica de los conjuntos

def diferencia (A,B,n,m):
  if n == 0:
      return []
  elif m == 0:
    C = []
    for i in range(0,n):
      C.append(A[i])
    return C
  elif A[n-1] == B[m-1]:
        return diferencia (A,B,n-1,m-1)
  elif A[n-1] > B[m-1]:
      return diferencia (A,B,n-1,m) + [A[n-1]]
  else:
      return diferencia (A,B,n,m-1)

# Pertenece

def conjuntos(A,x):
  bandera = False
  for i in range(len(A)):
    if A[i] == x:
      bandera = True
  return bandera

def pertenece(x,y):
  if x and y:
    return "Pertenece a ambos conjuntos"
  elif x:
    return "Pertenece solo al primero"
  elif y:
    return "Pertenece solo al segundo"
  else:
    return "NO pertenece a ninguno" 

# contiene 
def contenido (A):
  if len(A) == 0:
    bandera = True
  else:
    bandera = False
  return bandera   

def main():
  n = int(input("Digite la cantidad de elementos del primer conjunto: "))
  A = elementos(n)
  m = int(input("Digite la cantidad de elementos del segundo  conjunto:"))
  B = elementos(m)
  print("Digite un número para seleccionar una de las siguientes operaciones:")
  print("1 para UNION\n2 para INTERSECCIÖN\n3 para DIFRERENCIA\n4 para DIFRENECIA SIMËTRICA\n5 para PERTENECE\n6 para CONTENIDO\nCualquier otro número para salir")
  x = int(input("Opción: "))
  Concatenado = concatena(A,B)
  OrdenadoC = ordena(Concatenado,n+m)
  while 0<x<7:
    if x == 1:
      union = elimina_iguales(OrdenadoC)
      print("La unión de los conjuntos es: ", union)
      x = int(input("Seleccione otra opción: "))
    elif x == 2:
      Interseccion = repetidos(OrdenadoC)
      print("La interseccion de los conjuntos es",Interseccion)
      x = int(input("Seleccione otra opción: "))
    elif x == 3:
      ordenadoA = ordena(A,n)
      Interseccion = repetidos(OrdenadoC)
      m = len(Interseccion)
      Diferencia = diferencia(ordenadoA,Interseccion,n,m)
      print("La diferencia de los conjuntos es: ",Diferencia)
      x = int(input("Seleccione otra opción: "))
    elif x == 4:
      union = elimina_iguales(OrdenadoC)
      Interseccion = repetidos(OrdenadoC)
      l = len(union)
      k = len(Interseccion)
      simetrica = diferencia(union,Interseccion,l,k)
      print("La diferencia simétrica es", simetrica)
      x = int(input("Seleccione otra opción: "))
    elif x == 5:  
      num = int(input("Número que se comprobará si pertenece: "))
      prueba1 = conjuntos(A,num)
      prueba2 = conjuntos(B,num)
      pertenecen = pertenece(prueba1,prueba2)
      print(pertenecen)
      x = int(input("Seleccione otra opción: "))
    elif x == 6:
      ordenadoA = ordena(A,n)
      Interseccion = repetidos(OrdenadoC)
      m = len(Interseccion)
      Fin = diferencia(ordenadoA,Interseccion,n,m)
      contiene = contenido(Fin)
      print("¿A está contenido en B?", contiene)
      x = int(input("Seleccione otra opción: "))

  print("FIN")

main()



