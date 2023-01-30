def simple(K,i):
  s = K + (7*i)
  return s

def compuesto(K,i):
  c = K*((1 + (i/K))**7)
  return c

def main():
  K = float(input("Cantidad de dinero prestado: "))
  i = float(input("Cantidad de pesos de inetrés diario: "))

  print("El pago por interés simple es: ", simple(K,i))
  print("El pago por interés compuesto es: ", compuesto(K,i))

main()
