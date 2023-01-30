def Numero_huevos(A):
    H = A*8 / 3
    return H

def main():
  A = int(input("Numero de aves de la granja: " ))
  H = Numero_huevos(A)

  if(A > 3 and A % 6 ==0):
    print("La cantidad de huevos producidos en un mes son:", end =" ")
    print(H)
  else:
    print("La cantidad de aves debe ser mayor a 3 y multiplo de 6")

main()

