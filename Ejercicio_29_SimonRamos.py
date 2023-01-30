def elementos_A(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def elementos_B(p):
  B = []
  for i in range(0,p):
    i = float(input("Digite los números del arreglo: "))
    B.append(i)
  return B

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

def mediana(B,n):
  if n % 2 ==0:
    x = n//2
    med = (B[x] + B[x-1])/2
  else:
    med = B[n//2] 
  return med

def main():
  n = int(input("Digite la cantidad de elementos del arreglo de enetros: "))
  A = elementos_A(n)
  print("El arreglo ordenado es: ", ordena(A,n))
  B = ordena(A,n)
  print("Y la mediana del arreglo es: ", mediana(B,n))

  p = int(input("\nDigite la cantidad de elementos del arreglo de reales: "))
  C = elementos_B(p)
  print("El arreglo ordenado es: ", ordena(C,p))
  D = ordena(C,p)
  print("La mediana del arreglo es: ", mediana(D,p))

main()