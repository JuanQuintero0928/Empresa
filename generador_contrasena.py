import random


def generar_password(num_caracteres):
    num = ['1','2','3','4','5','6','7','8','9','0']
    letras_min = ['a','b','y','q','l','y','m','c']
    letras_may = ['U','E','B','P','B','C','Z']
    simb = ['@','?','!','=','#','%']
    lista = num + letras_min + letras_may + simb
    password = []

    for i in range(1,num_caracteres+1):
        caracter = random.choice(lista)
        password.append(caracter)

    password = "".join(password)
    return password


def run():
    print("GENERADOR DE CONTRASEÑAS")
    num_caracteres = int(input("Ingrese cuantos caracteres va tener la contraseña : "))
    
    password = generar_password(num_caracteres)
    print("Tu contraseña es : " + password)


if __name__ == '__main__':
    run()