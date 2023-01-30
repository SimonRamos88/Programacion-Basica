def venta(G,M,P):
  return (G+M+P)//3

def kilos(G,M,P,Y):
  if G > Y:
    return (Y * 50)/1000
  elif G+M > Y:
    return (G*20 +Y*30)/1000 
  else: 
    return (G*30 + M*10 + Y*20)/1000

def final(G,M,P):
  return kilos(G,M,P,venta(G,M,P))

def main():
  G = int(input("cantidad de escorpiones grandes: "))
  M = int(input("Cantidad de escorpiones medianos: "))
  P = int(input("Cantidad de escorpiones pequeños: "))

  while G<0 or M<0 or P<0:
    print("La cantidad de escorpiones no puede ser un número negativo, intente de nuevo.")
    G = int(input("cantidad de escorpiones grandes: "))
    M = int(input("Cantidad de escorpiones medianos: "))
    P = int(input("Cantidad de escorpiones pequeños: "))

  print("La cantidad de kilogramos que se pueden vender son:", final(G,M,P), "kg")

main()