def Hexagono_telaraña(R):
  valor = 6*R
  i = R
  while i >= 0:
    valor += 6*i
    i -= 1
  return valor

def main():
  R = float(input("Digite el valor del radio de la telaraña en centímetros: "))

  print("La cantidad de telaraña que necesita la araña para hacer su telaraña es: ", Hexagono_telaraña(R),"cm") 
  
main()
