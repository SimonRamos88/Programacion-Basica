def derivada_termino1(a):
  y = 2*a 
  return y

a = float(input("Coeficiente del termino elevado al cuadrado: "))
b = float(input("Coeficiente del termino lineal: "))
c = float(input("Coeficiente del termino independiente: "))
print("El coeficiente lineal es", derivada_termino1(a))