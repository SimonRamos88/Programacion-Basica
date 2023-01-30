def precio_madera(Q):
  return 4*Q

def precio_alambre(P):
  return 5*P

def precio_varilla(S):
  return 8*S



def material_económico(madera,alambre,varilla, cerca):   
    if cerca<= alambre and cerca<= varilla and cerca <= madera:
      return "cerca"
    elif alambre >= madera  and madera <= varilla and madera <= cerca:
      return "madera"
    elif madera >= alambre and alambre <= varilla and alambre <= cerca: 
      return "alambre"
    else:
      return "varillla"

def main():
  Q = float(input("Precio de la madera por metro: "))
  S = float(input("Precio de la varilla por metro: "))
  P = float(input("Precio del alambre de púas por metro: "))
  madera = precio_madera(Q)
  alambre = precio_alambre(P)
  varilla = precio_varilla(S)
  print("El material más económico es", material_económico(madera,alambre,varilla))

main()