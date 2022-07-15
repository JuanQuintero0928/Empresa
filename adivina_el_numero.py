import random

def run():
    aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un numero del 1 al 100 : "))

    while numero_elegido != aleatorio:
        if numero_elegido < aleatorio:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero : "))
    print("GANASTE")



if __name__ == '__main__':
    run()