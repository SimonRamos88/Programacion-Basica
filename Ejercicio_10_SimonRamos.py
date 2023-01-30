def evaluar_poli(a,b,c,x):
    imagen = a*x**2 + b*x + c
    return imagen

def main():
    a = float(input("Coeficiente del termino elevado al cuadrado: "))
    b = float(input("Coeficiente del termino lineal: "))
    c = float(input("Coeficiente del termino independiente: "))
    x = float(input("Valor dado a evaluar: "))
    print("La evaluacion del polinomio es", evaluar_poli(a,b,c,x))

main()