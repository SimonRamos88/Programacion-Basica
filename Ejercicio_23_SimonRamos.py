def elementos_A(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def sumar(A):
  suma=0
  for i in range(len(A)):
    suma += A[i]
  return suma

def elementos_B(m):
  B = []
  for i in range(0,m):
    i = float(input("Digite los números del arreglo: "))
    B.append(i)
  return B

def main():
  n = int(input("digite la cantidad de elementos del arreglo de enteros: "))
  A = elementos_A(n)
  print("\nLa suma de los elementos del arreglo de enteros es: ",sumar(A))
  m = int(input("\nDigite la cantidad de elementos del arreglo de reales: "))
  B = elementos_B(m)
  print("\nLa suma de los elementos del arreglo de reales es: ", sumar(B))

main()

