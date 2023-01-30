def arreglo(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del binario al revés: "))
    A.append(i)
  return A

def binario(A,n):
  if n ==1:
    return A[0]
  else:
    x = 2**(n-1) * A[n-1]
    return x + binario(A,n-1)
 
A = [0,0,1,1,1,0]

def main():
  n = int(input("Digite la cantidad de números del binario: "))
  A = arreglo(n)
  B = binario(A,n) 
  print("El decimal al cual se corresponde el arreglo es: ", B )
main()
