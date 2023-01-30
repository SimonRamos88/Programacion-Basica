def elementos(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def separa(A):
    B = []
    C = []
    for i in range(len(A)):
        if A[i] != 0:
            B.append(A[i])
        else:
            C.append(A[i])
    return B,C

def juntar(B,C):
    return B + C

def main():
  n = int(input("Digite la cantidad de elementos del arreglo de enetros: "))
  A = elementos(n)
  B,C = separa(A)
  print("El arreglo inicial es: ", A)
  print("El arreglo final es: ", juntar(B,C))
main()