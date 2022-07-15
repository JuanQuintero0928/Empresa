from turtle import st


def conversor(tipo_moneda, valor_moneda):
    valor = float(input("Cuantos pesos " + tipo_moneda + " tiene : " ))
    conversion = round((valor / valor_moneda),2)
    conversion = str(conversion)
    print("Usted tiene " + conversion + " pesos " + tipo_moneda )


print("""SELECCIONE UN TIPO DE MONEDA
1->  Pesos Colombianos
2->  Pesos Argentinos
3->  Pesos Mexicanos
4->  Euros
""")

opcion = int(input("ingrese numero : "))

if opcion == 1:
    conversor("colombianos",3793.17)
elif opcion == 2:
    conversor("argentinos",121.04)
elif opcion == 3:
    conversor("mexicanos",19.57)
elif opcion == 4:
    conversor("euros",4500)
else:
    print("Por favor seleccione una opcion valida.")
