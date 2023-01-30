def elementos_arreglo1(n):   
  A1 = []
  for i in range(0,n):
    i = int(input("Digite los números del PRIMER arreglo: "))
    A1.append(i)
  return A1

def elementos_arreglo2(n):
  A2 = []
  for i in range(0,n):
    i = int(input("Digite los numeros del SEGUNDO arreglo: "))
    A2.append(i)
  return A2

def producto_punto(A1,A2):
  suma = 0
  for i in range(len(A1)):
    suma += A1[i]*A2[i]
  return suma 

def elementos_arreglo1B(m):
  B1 = []
  for i in range(0,m):
    i = float(input("Digite los números del PRIMER arreglo: "))
    B1.append(i)
  return B1

def elementos_arreglo2B(m):
  B2 = []
  for i in range(0,m):
    i = float(input("Digite los numeros del SEGUNDO arreglo: "))
    B2.append(i)
  return B2

def producto_punto2(B1,B2):
  suma = 0
  for i in range(len(B1)):
    suma += B1[i]*B2[i]
  return suma 

def main():
  n = int(input("digite la cantidad de elementos de los arreglos de enteros: "))
  A1 = elementos_arreglo1(n)
  A2 = elementos_arreglo2(n)
  print("\nEl producto punto del arreglo de enteros es",producto_punto(A1,A2))
    
  m = int(input("\ndigite la cantidad de elementos de los arreglos de reales: "))
  B1 = elementos_arreglo1B(m)
  B2 = elementos_arreglo2B(m)
  print("\nEl producto punto de es",producto_punto2(B1,B2))

main()