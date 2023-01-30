def primo(x):
  bandera = True
  if x == 1:
    bandera = False
  else:
    n = 2
    while n < x and bandera:
      if x%n ==0:
        bandera = False
      n += 1
  return bandera

def main():
  x = int(input("Digite un número: "))
  print("¿",x, "es primo?", primo(x))

main()

