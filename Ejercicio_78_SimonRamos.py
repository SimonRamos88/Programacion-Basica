def corriparcial(cad,n):
  if n == 1:
    return cad[-1]
  else:
    return corriparcial(cad,n-1) + cad[n-2]

def corrimiento(cad):
    return corriparcial(cad, len(cad))

def main():
  cad = input("Ingrese la cadena: ")
  circularder = corrimiento(cad)
  print("el corrimiento circular a derecha es: ", circularder)
main()