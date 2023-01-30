def árboles(P,K,T):
  if T == 0:
    bandera = 0
  elif T % (P*K) != 0:
    bandera = T//(P*K) + 1
  else:
    bandera = T // (P*K)
  return bandera

def main():
  P = int(input("Cantidad de hojas por rama: "))
  K = int(input("Cantidad de ramas que quitaron por árbol: "))
  T = int(input("Cantidad de hojas que se desean obtener: "))

  print("Se deben podar", árboles(P,K,T), "árboles")

main()