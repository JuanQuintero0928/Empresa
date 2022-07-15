def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     if i == 5678:
    #         break
    #     print(i)

    # texto = input("Escribe un texto : ")
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    print("Tabla multiplicar")
    multiplicando = int(input("Digite el numero que desea multiplicar : "))
    numero = int(input("Digite hasta que numero se va a relizar la multiplicacion : "))

    for i in range(numero):
        result = multiplicando * i
        if result > 100:
            break
        print(str(multiplicando) + " * " + str(i) + " = " + str(result))




if __name__ == '__main__':
    run()