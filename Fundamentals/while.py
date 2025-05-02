datos = {}
continuar = True

while continuar:
    clave = input("Que dato vas a ingresar: ")
    valor = input(clave + ":")
    datos[clave] = valor
    print(datos)

    continuar = input("Deseas agregar mas datos (s/n): ") == 's'

print(datos)