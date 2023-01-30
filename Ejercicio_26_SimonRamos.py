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

def minimo1 (A,n):
  m = A[n-1]
  for i in range(n-1,-1,-1):
    if A[i] < m:
      m = A[i]
  return m

def minimo2 (B,p):
  m = B[p-1]
  for i in range(p-1,-1,-1):
    if B[i] < m:
      m = B[i]
  return m

def main():
  n = int(input("Digite la cantidad de elementos del arreglo de enteros: "))
  A = elementos_A(n)
  print("El mínimo elemento del arreglo de enteros es: ", minimo1(A,n))
  p = int(input("\nDigite la cantidad de elementos del arreglo de reales: "))
  B = elementos_B(p)
  print("El mínimo elemento del arreglo de reales es: ", minimo2(B,p))

main()
