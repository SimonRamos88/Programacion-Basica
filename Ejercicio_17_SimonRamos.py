# Figuras inscritas
def PerimetroCuadradoInscribe(R):
  return ((8*R)/1.4142)

def AreaCuadradoInscribe(R):
  return ((2*R)/1.4142)**2

def AreaPentagonoInscribe(R):
  return (5*(R**2) *0.726)/(0.726**2+1)

def PerimetroPentagonoInscribe(R):
  return (10*R*0.726*(1.236))/1.528

def AreaHexagonoInscribe(R):
  return (3*(R**2)*1.732)/2

def PerimetroHexagonoInscribe(R):
  return 6*R
# Figuras que circunscriben
def AreaCuadradoFuera(R):
  return 4*(R**2)

def PerimetroCuadradoFuera(R):
  return 8*R

def PerimetroPentagonoFuera(R):
  return(10*R*0.726)

def AreaPentagonoFuera(R):
  return 5*(R**2)*(0.726)

def PerimetroHexagonoFuera(R):
  return 12*R*0.577

def AreaHexagonoFuera(R):
  return 6*(R**2)*(0.577**2)*1.732

def main():
  R = float(input("Digite el valor del radio: "))

  print("\nFIGURAS INSCRITAS\n")

  print("El perimetro del cuadrado es: ", PerimetroCuadradoInscribe(R))
  print("El área del cuadrado : ", AreaCuadradoInscribe(R))
  print("El perimetro del pentagono es: ", PerimetroPentagonoInscribe(R))
  print("El área del pentagono es: ",  AreaPentagonoInscribe(R))
  print("El perimetro del hexagono es: ",PerimetroHexagonoInscribe(R))
  print("El área del hexagono es: ", AreaHexagonoInscribe(R))

  print("\nFIGURAS QUE INSCRIBEN A LA CIRCUNFERENCIA\n")

  print("El perimetro del cuadrado es: ", PerimetroCuadradoFuera(R))
  print("El área del cuadrado es: ", AreaCuadradoFuera(R))
  print("El perimetro del pentagono es: ", PerimetroPentagonoFuera(R))
  print("El área del pentagono es: ", AreaPentagonoFuera(R))
  print("El perimetro del hexagono es: ", PerimetroHexagonoFuera(R))
  print("El área del hexagono es: ", AreaHexagonoFuera(R))

main()