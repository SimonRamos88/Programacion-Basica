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

# determinante

def inter(A,i):
  n = len(A)
  j = i
  b = True
  while j<n and b:
    if A[j][i] != 0:
      A[i],A[j] = A[j],A[i]
      b = False
    j += 1
  return A

def reduce(A,i):
  n = len(A)
  m = len(A[0])
  piv = A[i][i]
  for j in range(m):
    A[i][j] /= piv
  for k in range(n):
    asigna = A[k][i]
    if k != i and asigna != 0:
      for j in range(m):
        A[k][j] -= asigna*A[i][j]
  return A, piv

def integra(A,x,i): 
  if A[i][i] == 0:
    A = inter(A,i)
    A,piv = reduce(A,i)
    x += 1
  else:
    A,piv = reduce(A,i)
  return A,piv,x

def toda2(A,x,i, det):
  if i < 1:
    return determinante(x,det)
  else:
    A,piv,x = integra(A,x,len(A)-i)
    det *= piv
    return toda2(A,x,i-1, det)

def determinante(x,det):
  if x % 2 ==0:
    return det
  else:
    return - det

def final(A):
  x = 0
  det = 1
  return toda2(A,x,len(A),det)

def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
    print("2 3 4\n5 6 7\n8 9 1")
    mat = input("ingrese la matriz a la cual se le calculará el determinante: ")
    A = matriz(mat)
    d = final(A)
    print("El determinante es: ", d)
main()