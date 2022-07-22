def max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

def run():
    num1 = int(input("Digite un numero : "))
    num2 = int(input("Digite otro numero : "))
    mostrar = max(num1, num2)
    print("el numero mayor es : " + str(mostrar))


if __name__=='__main__':
    run()