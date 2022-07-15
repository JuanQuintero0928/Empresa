def pedir_numeros():
    num1 = int(input("Numero 1 : "))
    num2 = int(input("Numero 2 : "))
    return(num1, num2)


def suma(numeros):
    operacion = 0
    for i in range(2):
        operacion += numeros[i]
    return operacion


def resta(numeros):
    operacion = 0
    for i in range(2):
        operacion = numeros[i] - operacion
    return operacion

def multiplicacion(numeros):
    pass

def division(numeros):
    pass



def run():
    print("""----------------Calculadora---------------------
            Seleccione una opcion para realizar la operacion
            1. SUMA
            2. RESTA
            3. MULTIPLICACION
            4. DIVISION
            5. SALIR
            """)
    calculo = int(input())
    if calculo < 0 or calculo > 5: 
        print("La opcion elegida es incorrecta.")
    elif calculo == 1:
        numeros = pedir_numeros()
        # print (numeros)
        total_suma = suma(numeros)
        print("El resultado de la suma es : " + str(total_suma))
    elif calculo == 2:
        numeros = pedir_numeros()
        total_resta = resta(numeros)
        print("El resultado de la resta es : " + str(total_resta))
    elif calculo == 3:
        numeros = pedir_numeros()
        total_multiplicacion = multiplicacion(numeros)
        print("El resultado de la multiplicacion es : " + str(total_multiplicacion))
    else:
        numeros = pedir_numeros()
        total_division = division(numeros)
        print("El resultado de la division es : " + str(total_division))
    


    


if __name__ == '__main__':
    run()