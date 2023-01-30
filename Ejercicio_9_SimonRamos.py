def suma(y,z):
    s = z + y
    return s

def multiplo(x,s):
  if (x<0 and s >0) or (x>0 and s<0):
    return False
  elif x%s != 0:
    return False
  else:
    return True 

def main():
  y = float(input("Digite el primer numero de la suma: "))
  z = float(input("Digite el segundo numero de la suma: "))
  x = float(input("Numero que se comprobara como multiplo: "))
  s = suma(y,z)
  print("¿",x, "es múltiplo de", s,"?", multiplo(x,s))

main()