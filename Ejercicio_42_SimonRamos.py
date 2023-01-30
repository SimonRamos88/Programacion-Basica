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

# Unión de los conjuntos
def union(A,B,n,m):
    if n == 0:
      C = []
      for i in range(0,m):
        C.append(B[i])
      return C
    elif m == 0:
      C = []
      for i in range(0,n):
        C.append(A[i])
      return C
    elif A[n-1] == B[m-1]:
      return union(A,B,n-1,m-1) + [A[n-1]]
    elif A[n-1] > B[m-1]:
      return union(A,B,n-1,m) + [A[n-1]]
    else:
      return union(A,B,n,m-1) + [B[m-1]]

# Intersección de los conjuntos
def interseccion (A,B,n,m):
    if n == 0 or m ==0:
        return []
    elif A[n-1] == B[m-1]:
        return interseccion(A,B,n-1,m-1) + [A[n-1]]
    elif A[n-1] > B[m-1]:
        return interseccion(A,B,n-1,m)
    else:
        return interseccion(A,B,n,m-1)

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
def contenido (A,C):
  if A == C:
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
  while 0<x<7:
    if x == 1:
      U = union(A,B,n,m)
      print("Union: ", U)
      x = int(input("Seleccione otra opción: "))
    elif  x == 2:
      inter = interseccion(A,B,n,m) 
      print("Intersección: ", inter)
      x = int(input("Seleccione otra opción: "))
    elif x == 3:
      dif = diferencia(A,B,n,m)
      print("La diferencia de los conjuntos es: ", dif)
      x = int(input("Seleccione otra opción: "))
    elif x == 4:
      U = union(A,B,n,m)
      N = interseccion(A,B,n,m) 
      l = len(U)
      k = len(N)
      sim = diferencia(U,N,l,k)
      print("La diferencia simétrica es", sim)
      x = int(input("Seleccione otra opción: "))
    elif x == 5:
      num = int(input("Número que se comprobará si pertenece: "))
      prueba1 = conjuntos(A,num)
      prueba2 = conjuntos(B,num)
      pertenecen = pertenece(prueba1,prueba2)
      print(pertenecen)
      x = int(input("Seleccione otra opción: "))
    elif x == 6:
      N = interseccion(A,B,n,m) 
      contiene = contenido(A,N)
      print("¿A está contenido en B?", contiene)
      x = int(input("Seleccione otra opción: "))
  print("FIN")

main()
            
