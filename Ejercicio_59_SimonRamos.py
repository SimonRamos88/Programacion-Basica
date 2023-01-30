# lecturas 
def arreglosreal(s):
  C = []
  d = ""
  n = len(s)
  for i in range(n):
    if s[i] == " ":
      if d != "":
        C.append(float(d))
      d = ""
    else:
      d += s[i]
  if d!= "":    
    C.append(float(d))
  return C

# Impresiones

def salida(C):
  n = len(C)
  m = len(C[0])
  e = ""
  d = ""
  for i in range(n):
    for j in range(m): 
      d += str(C[i][j])+ " "
    e += d + "\n"
    d = ""
  return e
# llenado en espiral
def arreglo(b,k):
  n = len(b) 
  a = 4*(k-1)
  x = n - k**2
  d = []
  for i in range(a):
    d.append(b[i+x])
  return d

def llena(A,d,k,j):
  x = (k-1)
  for i in range(k):
    A[j][i+j] = d[i]
    A[i+j][x+j] = d[x+i]
    A[x+j][x-i+j] = d[2*x+i]
    A[i+j][j] = d[-i]
  return A

def integra(A,b,n,j):
  if n <= 0:
    return A
  elif n == 1:
    A[j][j] = b[-1]
    return A
  else:
    return integra(llena(A,arreglo(b,n),n,j),b,n-2,j+1)

def espiral(b):
  n = int(len(b)**(0.5))
  A = [[0 for i in range(n)]for i in range(n)]
  return integra(A,b,n,n-n)

def main():
    print("para ingresar un arreglo, separe todos los elementos por medio de espacios, de esta forma, la entrada \" 2.5 4 5.2 3\" se corresponde con el arreglo [2.5, 4, 5.2, 3]")
    s = input("ingrese los elementos del arreglo, recuerden que la cantidad de elementos debe tener raíz cuadrada exacta: ")
    b = arreglosreal(s)
    esp = espiral(b)
    final = salida(esp)
    print("La matriz es: ")
    print(final)
main()