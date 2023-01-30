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
  return palindrome1(convierte(cad))

def main():
  cad = input("Digite la cadena: ")
  cadena= palindrome(cad)
  print("¿La cadena es palindrome?", cadena)
main()