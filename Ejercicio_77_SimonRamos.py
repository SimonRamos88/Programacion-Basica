def corriparcial(cad,n):
  if n == 1:
    return cad[0]
  else:
    return cad[-n+1] + corriparcial(cad,n-1)

def corrimiento(cad):
    return corriparcial(cad, len(cad))

def main():
  cad = input("Ingrese la cadena: ")
  circularizq = corrimiento(cad)
  print("el corrimiento circular a izquierda es: ", circularizq)
main()