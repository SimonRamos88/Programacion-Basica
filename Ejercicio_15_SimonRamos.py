def iguales(M1,M2,B1,B2):
  if M1== M2 and B1 == B2:
    bandera = True
  else:
    bandera = False
  return bandera 

def haysolucion(M1,M2):
  if M1==M2:
    bandera = False
  else:
    bandera = True
  return bandera 

def intersecta(M1,M2,B1,B2):
    x = (B1-B2)/(M2-M1)
    y = (M2*B1 -M1*B2)/(M2-M1)
    return x,y
  
def final(M1,M2,B1,B2):
  if iguales(M1,M2,B1,B2):
    return "Las rectas son las mismas e intersectan en infinitos puntos"
  elif haysolucion(M1,M2):
    return "El punto de intersección es " + str(intersecta(M1,M2,B1,B2))
  else:
    return "No hay punto de intersección"


def main():
  M1 = float(input("Digite la pendiente de la primera recta: "))
  B1 = float(input("Digite el punto de corte con el eje y de la primera recta: "))
  M2 = float(input("Digite la pendiente de la segunda recta: "))
  B2 = float(input("Digite el punto de corte con el eje y de la segunda recta: "))
  fin = final(M1,M2,B1,B2)
  print(fin)
main()
