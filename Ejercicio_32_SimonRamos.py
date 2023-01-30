def decimal(num):
    if num < 2:
        return [num]
    else:
        return [num % 2] + decimal(num//2)

def main():
    num = int(input("Digite el número entero no negativo a convertir a binario: "))
    print(decimal(num))
main()
