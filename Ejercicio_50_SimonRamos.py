# Lecturas

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

def matriz(s):
  D = []
  A = filas(s)
  m = len(A)
  for i in range(m):
    k = columnas(A[i])
    D.append(k)
  return D

def conviertereal(A):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      A[i][j] = float(A[i][j])
  return A

def convierteentero(A):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      A[i][j] = int(A[i][j])
  return A

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

# Suma

def suma(A,B):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      A[i][j] += B[i][j]
  return A

def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
    print("2 3 4\n5 6 7\n8 9 1")
    e1 = input("Digite la primera matriz (enteros): ")
    e2 = input("Digite la segunda matriz (enteros): ")
    A = convierteentero(matriz(e1))
    B = convierteentero(matriz(e2))
    se = suma(A,B)
    print("La suma de la matriz de enteros es: \n", salida(se))
    r1 = input("Digite la primera matriz (reales): ")
    r2 = input("Digite la segunda matriz (reales): ")
    C = conviertereal(matriz(r1))
    D = conviertereal(matriz(r2))
    sr = suma(C,D)
    print("La suma de la matriz de reales es: \n", salida(sr))
main()
