# Lecturas

def partir(p):
  s = []
  n = len(p)
  c = ""
  for i in range(n):
    if p[i] == "+" or p [i] == "-":
      if c!= "":
        s.append(c)
      c = ""
    c += p[i]
  s.append(c)
  return s

def coeficiente(t):
  s = ""
  n = len(t)
  i = 0
  while i<n and t[i] != "x":
    s += t[i]
    i += 1
  return float(s)

def coeficientes(ts):
  s = []
  n = len(ts)
  for i in range(n):
    s.append(coeficiente(ts[i]))
  return s

def exponente(t):
  n = len(t)
  if t[n-1]== "x":
    return 1
  k = 0
  while k<n and t[k] != "x":
    k+=1
  if k == n:
    return 0
  else:
    s = ""
    for i in range(k+2, n):
      s += t[i]
    return int(s)

def exponentes(ts):
  s = []
  n = len(ts)
  for i in range(n):
    s.append(exponente(ts[i]))
  return s

def maximo(A):
  n = len(A)
  m = A[n-1]
  for i in range(n-1,-1,-1):
    if A[i] > m:
      m = A[i]
  return m

def crearpolinomio(a,e):
  m = len(a)
  p = [0 for i in range(maximo(e)+1)]
  for i in range(m):
    p[e[i]] = a[i]
  return p

def polinomio(s):
  z = partir(s)
  return crearpolinomio(coeficientes(z),exponentes(z)) 

# Evaluación polinomio

def evalua(A,x):
    suma = 0
    for i in range(len(A)):
        suma += A[i] * x**i
    return suma

# suma de polinomios

def suma(A,B):
    if len(A) < len(B):
        return suma(B,A)
    else:
        for i in range(len(B)):
            A[i] = A[i] + B[i]
        return A    

# resta de polinomios
def cambia_signo(B):
    for i in range(len(B)):
        B[i] = -B[i]
    return B

def resta(A,B):
    return suma(A,cambia_signo(B)) 

# Multiplicación de polinomios

def filas(A,B,n,m):
    if m == -1:
        C = []
        for i in range(n):
            C.append(0)
        return C
    else:
        return filas(A,B,n,m-1) + [A[n]*B[m]]

def matriz(A,B,n,m):
    if len(A) > len(B):
        return matriz(B,A,m,n)
    elif n == -1:
        return []
    else:
        return matriz(A,B,n-1,m)+ [filas(A,B,n,m)]

def producto(C,k):
    if k == 0:
        return []
    else:
        return suma(C[k-1], producto(C,k-1)) 

def multiplicacion(A,B,n,m):
    return producto(matriz(A,B,n,m),len(matriz(A,B,n,m))) 

# division

def termino(A,B,n,m):
    if n < m:
        return []
    else:
        C = []
        for i in range(n-m):
            C.append(0)
        return C + [A[n]/B[m]]

def residuos(A,B):
    C = []
    for i in range(len(A)-1):
        C.append(A[i]-B[i])
    return C

def nuevodividendo(A,B):
    D = residuos(A, multiplicacion(B, termino(A,B,len(A)-1,len(B)-1) ,len(B)-1,len(A)-len(B)))
    return D

def division(A,B):
    if len(A) < len(B):
        return []
    else:
        return suma( termino(A,B,len(A)-1,len(B)-1), division(nuevodividendo(A,B),B))

# residuo de la división

def residuodiv(A,B):
    if len(A) < len(B):
        return A
    else:
        return residuodiv(nuevodividendo(A,B),B)
        
# impresiones

def mostrarpoli(A):
  if len(A)== 0:
    c = "0"
  else:
    c = str(A[0])
    for i in range(1,len(A)):
      if A[i] >= 0:
        c += (" + "+ str(A[i]) + "x^" + str(i))
      else:
        c += (" " + str(A[i])+"x^" + str(i))
  return c 

def main():
    print("Los polinomios deben ser escritos tomando el caracter “^” como simbolo que antecede al exponente, escribir todo el polinomio sin espacios, es necesario hacer explícito cada coeficiente. Un ejemplo de como debe escribirse es: “3x^2+2x+1”. ")
    s = input("Digite el primer polinomio: ")
    p = input("Digite el segundo polinomio: ")
    D = polinomio(s)
    E = polinomio(p)      
    print("Digite un número para seleccionar una de las siguientes operaciones:")
    print("1 para EVALUAR\n2 para SUMAR\n3 para RESTA\n4 para MULTIPLICAR\n5 para DIVIDIR\n6 para RESIDUO\nCualquier otro número para salir")
    x = int(input("Opción: "))
    while 0 < x <7:
        if x == 1:
            A = [x for x in D]
            B = [x for x in E]
            y = float(input("valor en el cual se evaluará el polinomio: "))
            primer_eva = evalua(A,y)
            segunda_eva = evalua(B,y)
            print("la evaliación del primer polinomio es: ", primer_eva)
            print("La evaluación del segundo polinomio es: ", segunda_eva)
            x = int(input("Seleccione otra opción: "))
        elif x == 2:
            A = [x for x in D]
            B = [x for x in E]
            sum = suma(A,B)
            s = mostrarpoli(sum)
            print("La suma de los polinomios es: ", s)
            x = int(input("Seleccione otra opción: "))
        elif x == 3:
            A = [x for x in D]
            B = [x for x in E]
            res = resta(A,B)
            r = mostrarpoli(res)
            print("La resta entre el primer polinomio y el segundo es: ", r)
            x = int(input("Seleccione otra opción: "))
        elif x == 4:
            A = [x for x in D]
            B = [x for x in E]
            n = len(A)-1
            m = len(B)-1
            multi = multiplicacion(A,B,n,m)
            z = mostrarpoli(multi)
            print("La multiplicación de los polinomios es: " , z)
            x = int(input("Seleccione otra opción: "))
        elif x == 5:
            A = [x for x in D]
            B = [x for x in E]
            div = division(A,B)
            d = mostrarpoli(div)
            print("La division de los polinomio es: ", d)
            x = int(input("Seleccione otra opción: "))
        elif x == 6:
            A = [x for x in D]
            B = [x for x in E]
            resi = residuodiv(A,B)
            re = mostrarpoli(resi)
            print("El residuo de la division es: ", re)
            x = int(input("Seleccione otra opción: "))
    print("FIN")        
main()

