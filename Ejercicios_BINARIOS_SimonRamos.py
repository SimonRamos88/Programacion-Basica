# lecturas

def filas(s):
  C = []
  n = len(s)
  d = ""
  for i in range(n):
    if s[i] == ",":
      C.append(d)
      d = ""
    else:
      d += s[i]  
  C.append(d)
  return C

def columnas(s):
  C = []
  d = ""
  n = len(s)
  for i in range(n):
    if s[i] == " ":
      if d != "":
        C.append(d)
      d = ""
    else:
      d += s[i]
  C.append(d)
  return C

def matrizbinaria(A):
  D = []
  m = len(A)
  for i in range(m):
    k = columnas(A[i])
    for j in range(len(k)):
      k[j] = int(k[j])
    D.append(k)
  return D

def matriz(s):
  return matrizbinaria(filas(s))

# Impresiones

def salida(C):
  n = len(C)
  m = len(C[0])
  e = ""
  d = ""
  for i in range(n):
    for j in range(m): 
      d += str(C[i][j])+ " "
    e += d + "\n"
    d = ""
  return e

# Unión

def union(A,B):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      if A[i][j] == 1 or B[i][j] == 1:
        A[i][j] = 1
  return A

def union2(A,B):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      if A[i][j] != B[i][j]:
        A[i][j] = 1
  return A

# Intersección

def interseccion(A,B):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      A[i][j] *= B[i][j]
  return A

# simetría 
def simetrica(A):
  i = 0
  v = True
  n = len(A)
  while i<n and v:
    j = 0
    while j<n and v:
      if A[i][j] == 1 and A[j][i] != 1:
        v = False
      j += 1
    i += 1
  return v

def simetrica2(A):
  i = 0
  v = True
  n = len(A)
  while i<n and v:
    j = 0
    while j<n and v:
      if A[i][j] != A[j][i]:
        v = False
      j += 1
    i += 1
  return v

# Reflexiva

def reflexiva(A):
  n = len(A)
  v = True
  i = 0
  while i<n and v:
    if A[i][i] == 0:
      v = False
    i += 1
  return v 

# Transitiva

def transitiva(A):
  n = len(A) 
  v = True
  i = 0
  while i<n and v:
    j = 0
    while j<n and v:
      if A[i][j] == 1:
        k = 0
        while k<n and v:
          if A[j][k] == 1:
            v = A[i][k] == 1
          k += 1
      j += 1
    i += 1
  return v

# Orden

def antisim(A):
  n = len(A)
  i = 0
  v = True
  while i <n and v:
    j = 0
    while j < n and v: 
      if i != j and A[i][j] == 1:
        v = A[j][i] == 0
      j += 1
    i += 1
  return v

def extra(A):
  n = len(A)
  v = True
  i = 0
  while i < n and v:
    j = 0
    while j < n and v:
      v = A[i][j] == 1 or A[j][i] == 1
      j += 1
    i += 1
  return v 

def parcial(A):
  return reflexiva(A) and transitiva(A) and antisim(A)

def total(A):
  return parcial(A) and extra(A)

def estricto(A):
  return not reflexiva(A) and not simetrica2(A) and transitiva

# Equivalencia

def equivalencia(A):
  return reflexiva(A) and simetrica2(A) and transitiva(A)

# Funcion

def sumafil(A,k):
  m = len(A[0])
  suma = 0
  for j in range(m):
    suma += A[k][j]  
  return suma

def funcion(A):
  n = len(A)
  i = 0
  while i<n and sumafil(A,i) <= 1:
    i += 1
  return i == n

# Inyectiva

def sumacol(A,k):
  n = len(A)
  suma = 0
  for i in range(n):
    suma += A[i][k]  
  return suma

def inyectiva(A):
  n = len(A)
  m = len(A[0])
  i = 0
  while i < n and sumafil(A,i) <= 1:
    i += 1
  j = 0
  if i == n:
    while j < m and sumacol(A,j) <= 1:
      j += 1
  return j == m    

# Sobreyectiva

def sobreyectiva(A):
  n = len(A)
  m = len(A[0])
  i = 0
  while i < n and sumafil(A,i) <= 1:
    i += 1
  j = 0
  if i == n:
    while j < m and sumacol(A,j) > 0:
      j += 1
  return j == m    

def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “1 0 1, 1 0 0, 0 1 1” representa a la matriz: ")
    print("1 0 1\n1 0 0\n0 1 1")
    print("Recuerde que si para porbar simetría, transitividad, equivalencia, reflexividad y orden la relación debe ser de un conjunto sobre sí mismo, por lo que la matriz de la relació deberá ser cuadrada")
    s = input("Porfavor ingresa la primera matriz (relación): ")
    A = matriz(s)
    q = input("Porfavor ingresa la segunda matriz (relación):")
    B = matriz(q)
    print("Escoge alguna de las siguientes opciones: ")
    print("1 para UNION\n2 para INTERSECCION\n3 para SIMETRIA\n4 para REFLEXIVIDAD\n5 para TRANSITIVIDAD\n6 para ORDEN\n7 para EQUIVALENCIA\n8 para FUNCION\n9 para INYECTIVIDAD\n10 para SOBREYECTIVIDAD\nOtro para salir")
    x = int(input("Su opción: "))
    while 1<=x<=10:
        if x == 1:
            C = [[x for x in A[x]]for x in range(len(A))]
            D = [[x for x in B[x]]for x in range(len(B))]
            U = union2(C,D)
            print("La unión de las matrices es: ")
            print(salida(U))
            x = int(input("Otra opción: "))
        elif x == 2:
            C = [[x for x in A[x]]for x in range(len(A))]
            D = [[x for x in B[x]]for x in range(len(B))]
            N = interseccion(C,D)
            print("La intersección es: ")
            print(salida(N))
            x = int(input("Otra opción: "))
        elif x == 3:
            sim = simetrica2(A)
            print("¿la primera relación es simétrica? ", sim)
            x = int(input("Otra opción: "))
        elif x == 4:
            ref = reflexiva(A)
            print("¿la primera relación es reflexiva? ", ref)
            x = int(input("Otra opción: "))
        elif x == 5:
            tran = transitiva(A)
            print("¿La primera relación es transitiva? ", tran)
            x = int(input("Otra opción: "))
        elif x == 6:
            parci = parcial(A)
            tot = total(A)
            est = estricto(A)
            print("¿La primera relación es de orden parcial? ", parci)
            print("¿Es de orden total? ", tot)
            print("¿Es de orden estricto? ", est)
            x = int(input("Otra opción: "))
        elif x == 7:
            equi = equivalencia(A)
            print("¿La primera relación es de equivalencia? ", equi)
            x = int(input("Otra opción: "))
        elif x == 8:
            fun1 = funcion(A)
            fun2 = funcion(B)
            print("¿La primera relación es función?", fun1)
            print("¿La segunda relación es función? ", fun2)
            x = int(input("Otra opción: "))
        elif x == 9:
            iny1= inyectiva(A)
            iny2 = inyectiva(B)
            print("¿La primera relación es función inyectiva?", iny1)
            print("¿La segunda relación es función inyectiva? ", iny2)
            x = int(input("Otra opción: "))
        else:
            sob1= sobreyectiva(A)
            sob2 = sobreyectiva(B)
            print("¿La primera relación es función sobreyectiva?", sob1)
            print("¿La segunda relación es función sobreyectiva? ", sob2)
            x = int(input("Otra opción: "))
main()

