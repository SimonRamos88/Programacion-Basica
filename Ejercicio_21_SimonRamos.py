def fichas1(n):
  if(n ==2):
    return 2

  elif(n==1):
    return 1

  elif(n==0):
    return 0

  else:
    return fichas1(n-1) + fichas1(n-2) 

def fichas2(n):
  if(n==3):
    return 4

  elif(n==2):
    return 2

  elif(n==1):
    return 1

  elif(n==0):
    return 0

  else: 
    return fichas2(n-1)+fichas2(n-2) + fichas2(n-3)

def main():   
  n = int(input("Digite el largo de la base: "))
    
  print("Hay",fichas1(n), end=" ")
  print("formas con solo fichas rojas y azules")
  print("Y",fichas2(n), "formas con fichas rojas, azules y amarillas")

main()
