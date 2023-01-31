def decimalUno():
    entrada= input("ingrese cordenadas:")
    partes= entrada.split(".") #dividimos la cadena por el punto

    if len(partes[1]) == 3:
        print(partes[1])
    else:
        print("el dato no contiene 3 decimales")
    print(len(partes[1]))

def decimalDos():
    entrada = float(input("ingrese cordenadas:"))
    redondeado= round(entrada,3)
    if redondeado != entrada: # esto significa que ingreso menos de 3 decimales
        print("Ingrese el dato con tres decimales")
    else:
        print("super: ", redondeado)

decimalUno()
