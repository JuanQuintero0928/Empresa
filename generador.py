import random


def generar_pass(caracteres):
        num = ['1','2','3','4','5','6','7','8','9','0']
        min = ['a','b','c','d','e','f','g','h','i','j','k']
        may = ['A','B','C','D','E','F','G','H','I','J','K']
        simb = ['#','&','(',')','/','@','!','¡','?','¿']
        lista = num + min + may + simb
        password = []

        for i in range (1,caracteres+1):
            caracter_random = random.choice(lista)
            password.append(caracter_random)
            
        password = "".join(password)
        return password


def run():
    caracteres = int(input("Ingrese el numero de caracteres que quiere la contraseña : "))
    password = generar_pass(caracteres)
    print("Nueva contraseña : " + password)

if __name__ == '__main__':
    run()