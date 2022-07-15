import random

def run():
    aleatorio = random.randint(1,100)
    opcion = int(input("Elige Opcion:  1- Jugar   2-Salir  : "))
    while opcion == 1:
        numero_elegido = int(input("Elige un numero del 1 al 100 : "))
        while numero_elegido != aleatorio:
            if numero_elegido < aleatorio:
                print("Busca un numero mas grande")
            else:
                print("Busca un numero mas pequeño")
            numero_elegido = int(input("Elige otro numero : "))
        print("GANASTE")
        opcion = int(input("Elige Opcion:  1- Jugar   2-Salir : "))
    print("Saliendo...")

if __name__ == '__main__':
    run()