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

def matriz(s):
  return matrizreales(filas(s))

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

# inversa 

def identidad(A):
  n = len(A)
  B = []
  for j in range(n):
    B1 =[]
    for i in range(n):
      if i != j:
        B1.append(0)
      else:
        B1.append(1)
    B.append(B1)
  return B

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
    B[i][j] /= piv
  for k in range(n):
    asigna = A[k][i]
    if k != i and asigna != 0:
      for j in range(m):
        A[k][j] -= asigna*A[i][j]
        B[k][j] -= asigna*B[i][j]
  return A,B

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

def inversa(A):
  return toda(A,identidad(A),len(A))

def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
    print("2 3 4\n5 6 7\n8 9 1")
    mat = input("ingrese la matriz a la cual se le calculará la inversa: ")
    A = matriz(mat)
    inv = inversa(A)
    fin = salida(inv)
    print("La inversa es: ")
    print(fin)

main()