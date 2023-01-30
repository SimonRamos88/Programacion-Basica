def potencia(B,E):
  bandera = 1
  if E<0:
    while E<0:
      bandera *= B
      E += 1
    return 1/bandera 
  elif E>0:
    while E>0:
      bandera *= B
      E -= 1
    return bandera
  else:
    return bandera

def main():
  B = int(input("digite la base (número entero): "))
  E = int(input("digite el exponente (número entero): "))

  if E <= 0 and B == 0:
    print("Valor indeterminado")
  else:
    print("El resultado es", potencia(B,E))

main()
