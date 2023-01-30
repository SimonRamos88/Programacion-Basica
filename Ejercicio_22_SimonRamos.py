def crea(n):
  A = [False,False]
  n += 1
  while n > 2:
    A.append(True)
    n -= 1
  return A

def tacha(A,n):
  k = 2
  while(k<n):
    if A[k] == True:
      for i in range(2,n//k+1):  
        A[k*i] = False
    k += 1
  return A

def imprime(A):
  c = []
  for i in range(len(A)):
    if A[i] == True:
      c.append(i)
  return c

def main():
  n =int(input("Digite hasta que número se calculara la criba: "))
  A = crea(n)
  B = tacha(A,n)
  print(imprime(B))

main()