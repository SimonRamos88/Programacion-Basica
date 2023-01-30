def elementos_A(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def promedioA(A,n):
  suma=0
  for i in range(0,n):
    suma += A[i]
  return suma//n

def elementos_B(m):
  B = []
  for i in range(0,m):
    i = float(input("Digite los número del arreglo: "))
    B.append(i)
  return B

def promedioB(B,m):
  suma2 = 0
  for i in range(0,m):
    suma2 += B[i]
  return suma2/m

def main():
  n = int(input("digite la cantidad de elementos del arreglo de enteros: "))
  A = elementos_A(n)
  print("\nEl proemdio de los elementos del arreglo de enteros es: ",promedioA(A,n))

  m = int(input("\nDigite la cantidad de elementos del arreglo de reales: "))
  B = elementos_B(m)
  print("\nEl promedio de los elementos del arreglo de reales es: ", promedioB(B,m))

main()
