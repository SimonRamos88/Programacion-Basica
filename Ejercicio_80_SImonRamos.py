def posicion(cr,con):
  m = len(con)
  p = 0
  while p <m and con[p] != cr:
    p += 1
  return p 

def decodifica(dec,cor):
  n = len(dec)
  m = len(cor)
  c = ""
  for i in range(n):
    k = posicion(dec[i],cor)
    if k == 14:
      c += "ñ" 
    elif ("a" <= dec[i] <= "z" or dec[i] == "ñ" ) and k != m:
      if k < 14:
        c += chr(k + 97) #Se suma 97 porque este es el código ASCII de la letra "a"
      else:
         c += chr(k + 96)
    else:
      c += dec[i]
  return c

def main():
  dec = input("cadena a decodificar: ")
  cor = input("Cadena de correspondencia: ")
  final = decodifica(dec,cor)
  print("la cadena decodificada es: ", final)
main()