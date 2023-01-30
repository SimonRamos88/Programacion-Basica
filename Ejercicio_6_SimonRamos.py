def divisible(x,y):
    if y == 0:
        return False
    elif x % y != 0:
        return False 
    else: 
        return True 

def main():
    x = float(input("Digite el primer numero: "))
    y = float(input("Digite el número por el cual se dividira: "))
    print("¿",x, "es divisible por",y ,"?", divisible(x,y))

main()
