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

# Matriz mágica
def sumacol(A,k):
  n = len(A)
  suma = 0
  for i in range(n):
    suma += A[i][k-1]  
  return suma

def sumafil(A,k):
  m = len(A[0])
  suma = 0
  for j in range(m):
    suma += A[k-1][j]  
  return suma

def diagonal(A):
  n = len(A)
  suma1 = 0
  suma2 = 0
  for i in range(n):
    suma1 += A[i][i]
    suma2 += A[i][-(i+1)]  
  return [suma1] + [suma2]

def iguales(A,k):
  n = len(A)
  i = 0
  v = True
  while i<n and v:
    if sumacol(A,i) != k and sumafil !=k:
      v = False
    i += 1
  return v

def sumaigual(A,B):
  if B[0] == B[1]:
    v = iguales(A,B[0])
  else:
    v = False
  return v

def magica(A):
  return sumaigual(A,diagonal(A))

def main():
  print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
  print("2 3 4\n5 6 7\n8 9 1")
  s = input("ingrese la matriz: ")
  A = matriz(s)
  mag = magica(A)
  print("¿La matriz es mágica?: ", mag)
main()