def fibo(x):
  F1= 0
  F2= 1
  while x>=F1 or x>=F2:
    if(x == F1 or x == F2):
      return True  
    F1 = F1 + F2
    F2 = F1 + F2
  return False

def main():
  x = int(input("Digite el número NATURAL a comprobar: "))
  print("¿",x,"es un numero de fibonacci?", fibo(x))

main()
 