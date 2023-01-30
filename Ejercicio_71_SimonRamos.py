def ocurrencia(x,cad):
    y = 0
    for i in cad:
        if i == x:
            y += 1
    return y

def main():
    x = input("Caracter: " )
    cad = input("Cadema: ")
    ocurre = ocurrencia(x,cad)
    print("El número de ocurrencias es: ", ocurre)

main()