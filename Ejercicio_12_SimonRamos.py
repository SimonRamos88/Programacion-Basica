def derivada(a,x,b):
  y = 2*a*x + b
  return y

a = float(input("Coeficiente del termino elevado al cuadrado: "))
b = float(input("Coeficiente del termino lineal: "))
c = float(input("Coeficiente del termino independiente: "))
x = float(input("Valor en el cual se elebara la derivada: "))

print("El resultado de evaluar la derivada es:", end=" ")
print(derivada(a,x,b))