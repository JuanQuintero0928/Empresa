def run():
    caracteres = input("Digite la cadena de parentesis : ")
    lista_caracteres = list(caracteres)
    # print(lista_caracteres)

    longitud = len(lista_caracteres)
    # print(longitud)
    var_suma = 0

    if longitud % 2 != 0:
        print(False)
    elif lista_caracteres[0] == '(':
        for i in range(longitud):
            validacion = lista_caracteres[i]
            if validacion == '(' and var_suma >= 0:
                var_suma = var_suma + 1
            elif validacion == ')' and var_suma >= 0:
                var_suma = var_suma - 1

        if var_suma != 0:
            print(False)
        else:
            print(var_suma)
            print(True)
    else:
        print(False)


if __name__=='__main__':
    run()
