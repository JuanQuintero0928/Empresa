import statistics

def validar(num):

    if num > 4 and num < 16:
        return True
    else:
        return False


def run():
    print("Se ingresa por teclado 10 pares de temperaturas (T1 y T2) para hallar el promedio de las temperaturas que estan entre 5° y 15° (incluidos)")
    
    cantidad = 2
    lista = []
    for i in range(cantidad):
        num1 = int(input("Digite temperatura 1 : "))
        num2 = int(input("Digite temperatura 2 : "))
        
        if validar(num1):
            lista.append(num1)

        if validar(num2):
            lista.append(num2)

    # print(lista)
    media = statistics.mean(lista)
    print("La temperatura promedio es de : " + str(media))


if __name__ == '__main__':
    run()
