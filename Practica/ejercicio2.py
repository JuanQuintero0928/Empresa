def run():

    lista = []
    
    for i in range(4):
        num = int(input("Ingrese un numero : "))
        lista.append(num)

    print(lista)
    
    i = 0
    while i < len(lista):
        if lista[i] < 0:     
            print(lista[i], end=" ")
        i += 1
        
    while i < len(lista):
        if 0 < lista[i] and 10 > :
            print(lista[i], end = " ")
        i += 1

if __name__ == '__main__':
    run()