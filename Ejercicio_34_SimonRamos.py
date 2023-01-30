def elementos_A(n):
  A = []
  for i in range(0,n):
    i = int(input("Digite los números del arreglo: "))
    A.append(i)
  return A

def mcd(x,y):
  if y > x:
    return mcd(y,x)
  elif y ==0:
    return x
  else:
    return mcd(y,x%y)

def mcm(x,y):
  min = (x*y)//mcd(x,y)
  return min

def minimocomun(A,n,m):
  if n < 3:
    return m
  else: 
    m = mcm(A[n-3],m)
    return minimocomun(A,n-1,m)

def main():
  n = int(input("Digite la cantidad de elementos del arreglo de enteros: "))
  A = elementos_A(n)
  m = mcm(A[n-1],A[n-2])
  min = minimocomun(A,n,m)
  print("El máximo común divisor es: ", min)

main()