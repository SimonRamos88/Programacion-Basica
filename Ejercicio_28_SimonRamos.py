def elementos_A1(n):
  A1=[]
  for i in range(0,n):
    i = int(input("Digite los elementos del PRIMER arreglo: "))
    A1.append(i)
  return A1

def elementos_A2(n):
  A2=[]
  for i in range(0,n):
    i = int(input("Digite los elementos del SEGUNDO arreglo: "))
    A2.append(i)
  return A2

def producto_directoA(A1,A2):
  PDA = []
  for i in range(len(A1)):
    c = A1[i]*A2[i]
    PDA.append(c)
  return PDA 

def elementos_B1(m):
  B1=[]
  for i in range(0,m):
    i = float(input("Digite los elementos del PRIMER arreglo: "))
    B1.append(i)
  return B1

def elementos_B2(m):
  B2 = []
  for i in range(0,m):
    i = float(input("Digite los elementos del SEGUNDO arreglo: "))
    B2.append(i)
  return B2

def producto_directoB(B1,B2):
  PDB=[]
  for i in range(len(B1)):
    c = B1[i]*B2[i]
    PDB.append(c)
  return PDB

def main():
  n = int(input("Ingrese la cantidad de elementos de los arreglos de enteros: "))
  A1 = elementos_A1(n)
  A2 = elementos_A2(n)
  print("El producto directo de los arreglos de enteros", producto_directoA(A1,A2))

  m = int(input("\nIngrese la cantidad de elementos de los arreglos de reales: "))
  B1 = elementos_B1(m)
  B2 = elementos_B2(m)
  print("El producto directo de los arreglos de reales", producto_directoB(B1,B2))

main()