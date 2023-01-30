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

def matrizreales(A):
  D = []
  m = len(A)
  for i in range(m):
    k = columnas(A[i])
    for j in range(len(k)):
      k[j] = float(k[j])
    D.append(k)
  return D

def arregloreal(A):
    n = len(A)
    for i in range(n):
        A[i] = float(A[i])
    return A

def arreglo(s):
    return arregloreal(columnas(s))

def matriz(s):
  return matrizreales(filas(s))

# solución de ecuaciones

def inter(A,B,i):
  n = len(A)
  j = i
  b = True
  while j<n and b:
    if A[j][i] != 0:
      A[i],A[j] = A[j],A[i]
      B[i],B[j] = B[j], B[i]
      b = False
    j += 1
  return A,B

def reduce(A,B,i):
  n = len(A)
  m = len(A[0])
  piv = A[i][i]
  for j in range(m):
    A[i][j] /= piv
  B[i] /= piv
  for k in range(n):
    asigna = A[k][i]
    if k != i and asigna != 0:
      for j in range(m):
        A[k][j] -= asigna*A[i][j]
      B[k] -= asigna*B[i]
  return A,B

def Gauss(A,B):
  n = len(A)
  for i in range(n):
    if A[i][i] == 0:
      A,B = inter(A,B,i)
      A,B = reduce(A,B,i)
    else:
      A,B = reduce(A,B,i)
  return B

# definición recursiva
def integra(A,B,i):
  if A[i][i] == 0:
    A,B = inter(A,B,i)
    A,B = reduce(A,B,i)
  else:
    A,B = reduce(A,B,i)
  return A,B

def toda(A,B,i):
  if i < 1:
    return B
  else:
    A,B = integra(A,B,len(B)-i)
    return toda(A,B,i-1)

def Gauss2(A,B):
  return toda(A,B,len(B))

def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
    print("2 3 4\n5 6 7\n8 9 1")
    mat = input("ingrese la matriz del sistema de ecuaciones lineales (coeficientes de las variables): ")
    arr = input("Ingrese el arreglo con las igualdades de cada ecuación: ")
    A = matriz(mat)
    B = arreglo(arr)
    sol = Gauss(A,B)
    print("La solución al sistema es: ", sol)   
    #print("======")
    # recursiva
    #D = matriz(mat)
    #C = arreglo(arr)
    #print(Gauss2(D,C))
main()