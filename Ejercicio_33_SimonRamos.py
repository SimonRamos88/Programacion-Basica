def elementos_A(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def min (A,n):
  x = A[n-1]
  indice = n-1
  for i in range(n-1,-1,-1):
    if A[i] < x:
      x = A[i]
      indice = i
  return indice

def ordena(A,n):
  while n>1:
    x = A[min(A,n)]
    A[min(A,n)] = A[n-1]
    A[n-1] = x
    n -= 1
  return A
  
def ceros(B):
  x = 0
  for i in range(len(B)):
    if B[i] == 0:
      x += 1
  return x

def modulos(B,x):
  B = ordena(B,len(B))
  for i in range((len(B)-1)-x):
    B[i] = B[i]%B[i+1]
  return B

def mcd(B):
  B = ordena(B,len(B))
  if B[1]==0:
    return B[0]
  else:
    return mcd(modulos(B,ceros(B)))

def main():
  n = int(input("Digite la cantidad de elementos del arreglo de enteros: "))
  A = elementos_A(n)
  B = ordena(A,n)
  maximo = mcd(B)
  print("El máximo común divisor es: ", maximo)

main()