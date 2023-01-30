def ocurrencia(x,cad):
    y = 0
    for i in cad:
        if i == x:
            y += 1
    return y

def contenido(cad1,cad2):
    i = 0
    bandera = True
    while i < len(cad1) and bandera:
        x = cad1[i]
        if ocurrencia(x,cad1) > ocurrencia(x,cad2):
            bandera = False
        else:
            i += 1
    return bandera 

def main():
    cad1 = input("Digite la primer a cadena: ")
    cad2 = input("Digite la segunda cadena: ") 
    conti = contenido(cad1,cad2)
    print("¿La primera cadena está contenida en la segunda?: ", conti)
main()

