def codifica(cad,cor):
  n = len(cad)
  m = len(cor)
  c = ""
  for i in range(n):
    k = ord(cad[i]) - 97 #Se resta 97 pues este es el código ASCII de la "a"
    if cad[i] == "ñ":
      c += cor[14]
    elif ("a" <= cad[i] <= "n") and k<m:
      c += cor[k]
    elif ("o" <= cad[i] <= "z") and k<m:
      c += cor[k+1] 
    else:
      c += cad[i]
  return c

def main():
  cad = input("Digite la cadena: ")
  cor = input("Digite la cadena de correspondencia: ")
  codi = codifica(cad,cor)
  print("la cadena codificada es: ", codi)
main()