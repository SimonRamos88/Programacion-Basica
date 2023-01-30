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

# suma fila
def sumafil(A,k):
  m = len(A[0])
  suma = 0
  for j in range(m):
    suma += A[k-1][j]  
  return suma
  
def main():
    print("Al digitar las matrices utilice una “,” para separar a las filas entre sí y un espacio entre los números para separar a los números que conformarían a las columnas, de esta forma la entrada  “2 3 4, 5 6 7, 8 9 1” representa a la matriz: ")
    print("2 3 4\n5 6 7\n8 9 1")
    s = input("ingrese la matriz: ")
    k = int(input("¿Qué fila desea sumar?: "))
    A = matriz(s)
    suma = sumafil(A,k)
    print("la suma de los elementos de la fila es: ", suma)
main()