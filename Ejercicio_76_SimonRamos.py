def espacios(cad):
  s = ""
  n = len(cad)
  for i in range(n):
    if cad[i] != " ":
      s += cad[i]
  return s 
def convierte(cad):
  minus = ""
  n = len(cad)
  A = ord("A")
  a = ord("a")
  for i in range(n):
    if "A"<= cad[i] <= "Z":
      minus += chr(ord(cad[i])-A +a)
    else:
      minus += cad[i]
  return minus

def palindrome1(cad):
  i = len(cad)
  while i > (len(cad)//2)  and cad[-i] == cad[i-1]:
    i -= 1
  return i == (len(cad) // 2) 

def palindrome(cad):
  return palindrome1(convierte(espacios(cad)))

def main():
  cad = input("Digite la cadena: ")
  cadena= palindrome(cad)
  print("¿La cadena es frase palíndrome?", cadena)
main()