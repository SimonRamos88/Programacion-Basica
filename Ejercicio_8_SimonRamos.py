def relativos(x,y):
  n = 2
  while n <= x:
    if(x % n == 0 and y % n ==0):
      return False    
    n += 1
  return True

def main():
  x = int(input("Digite un numero: "))
  y = int(input("Digite un segundo numero: "))
  print("¿",x,"y", y, "son primos relativos ?", relativos(x,y))
  
main()
