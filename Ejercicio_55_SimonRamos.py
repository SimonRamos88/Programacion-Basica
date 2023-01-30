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

# impresiones

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

# Asignación de mayores

def mayores(A,x):
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      if A[i][j] > x:
        A[i][j] = 1
      else:
        A[i][j] = 0
  return A

def main():
  print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
  print("2 3 4\n5 6 7\n8 9 1")
  s = input("ingrese la matriz: ")
  A = matriz(s)
  x = int(input("Digite el número con el cual va a comparar: "))
  B = mayores(A,x)
  nueva = salida(B)
  print("La nueva matriz es:")
  print(nueva)
main()