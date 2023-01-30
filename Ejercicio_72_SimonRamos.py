def fragmento(cad,ini,fin):
    c = ""
    for i in range(ini,fin):
        c += cad[i]
    return c

def subcadena(sub,cad,x):
  if x < len(sub):
    return False
  else: 
    return fragmento(cad,x-len(sub),x) == sub or subcadena(sub,cad,x-1)
  

def main():
    sub = input("Primer cadena: ")
    cad = input("Segunda cadena: ")
    x = len(cad)
    solucion = subcadena(sub,cad,x)
    print("¿la primera cadena es subcadena de la segunda?: ", solucion)
    
main()
                
