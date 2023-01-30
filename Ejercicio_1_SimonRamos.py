def Litros_prod(V,N,M,P):
    z = ((N*M)/P)*V
    return z

def main():
  V = int(input("Numero de vacas: "))
  M = float(input("Largo del corral de las vacas en metros:  "))
  N = float(input("Ancho del corral de las vacas en metros: "))
  P = float(input("Metros cuadrados de pasto necesarios para producir 1 litro de leche: "))

  if( V<=0 or M<=0 or N<=0 or P<=0):
    print("Error al introducir los datos, ninguno puede ser menor o igual a 0")
    print("Intentelo de nuevo")
  else: 
    print("Los litros producidos son: ", end = "")
    print(Litros_prod(V,N,M,P), "litros")
main()
