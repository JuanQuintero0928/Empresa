def validad_edad(edad):
    if edad > 17:
        return True
    else:
        return False


def run():
    edad = int(input("Ingrese su edad : "))
    if edad < 0:
        print("La edad no es correcta.")
    elif validad_edad(edad):
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")


if __name__=='__main__':
    run()