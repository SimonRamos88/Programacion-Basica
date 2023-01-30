def sonpar_per(M1,M2,B1,B2):
  if M1 == M2 and B1 != B2:
    valor =  "son paralelas"
  elif M1*M2 == -1:
    valor = "son perpendiculares"
  else: 
    valor = "no son ni paralelas ni perpendiculares"
  return valor

def main():
  M1 = float(input("Digite la pendiente de la primera recta: "))
  B1 = float(input("Digite el punto de corte con el eje y de la primera recta: "))
  M2 = float(input("Digite la pendiente de la segunda recta: "))
  B2 = float(input("Digite el punto de corte con el eje y de la segunda recta: "))

  print(sonpar_per(M1,M2,B1,B2))

main()