def area_triangulo(R):
    valor = (18*R**2)/(2*1.732)
    return valor
def main():
    R = int(input("Digite el valor del radio de la circunferencia (en centímetros): "))
    print( "El área del triangulo es: ", area_triangulo(R), "cm")

main()