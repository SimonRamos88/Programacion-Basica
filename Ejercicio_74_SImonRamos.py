def invierte(cad,x):
    if x == 1:
        return cad[0]
    else:
        return cad[x-1] + invierte(cad,x-1)

def final(cad):
    return invierte(cad,len(cad))

def main():
    cad = input("Cadena a invertir: ")
    invertida = final(cad)
    print("La cadena invertida es: ", invertida)
main()