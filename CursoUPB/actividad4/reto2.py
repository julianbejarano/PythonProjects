import os

"""
RETO 2.
Este programa se encarga de la ordenacion de una lista segun el interes del usuario,
es imPortante aclarar que la lista se ordena cada vez que el usuario accede a su midificacion,
por lo tanto, la lista toma un orden básico y luego lo modifica segun la opcion ingresada,
si el usuario se equivoca 3 veces consecutivas en la eleccion del menú inicial, el programa
envia el mensaje error y se termina su ejecución.

By: Julian Dario Bejarano Gomez
Id: 000468882
código del curso: 51671

"""

#esta variable la usaremos para verificar el numero de intentos del usuario
intentos= 1

# Funcion de adivinanzas para verificar por segunda vez el ingreso de datos
def adivinanzas():

    adiv1=int(input("“Para confirmar por favor responda: Que número mayor que cero pero menor que 2:\n"))
    if adiv1 ==1:
        adiv2=int(input("“Para confirmar por favor responda: Cuantos cerebros posee un humano:\n"))
        if adiv2 == 1:
            os.system("cls")
            return True
        else:
            print("Error")
            menu()
    else:
        print("Error")
        menu()

def menuInicial():
    """
    primero definimos que vamos a utilizar la variable global definida al inicio del codigo
    y que lleva por nombre "intentos", por lo tanto la llamamos y modificamos, gracias al
    llamado "global"
    """
    global intentos

    """
    lo que haremos en esta funcion será:
    1: pedimos la opcion que desea realizar el usuario.

    2: Verificamos si la opcion esta en el rango de opciones (1-7)
        - si es la 7 cerramos el programa.
        - si es la 6, llamamos a la funcion de ordenar el funcion en base al favorito
        - si es del 1 al 5 enviamos el mensaje de la opción elegida y cerramos el programa

    3: Si la opción no esta dentro del rango: 1-7, verificamos el numero de intentos fallidos
       que ha ingresado el usuario a la plataforma, si este ha hecho 3 errores consecutivos
       se cierra el programa.
    """

    opc = int(input("Elija una opción:\n"))
    # print("Haz elegido la opción: ", str(opc))

    if opc <8 and opc> 0:

        if opc == 7:
            print("Hasta pronto")
            os.system("pause")
            return False

        elif opc == 6:
            # reiniciamos el valor de intentos  1, para eliminar su consecutividad
            intentos = 1
            """Preguntamos cual es la opcion favorita, la
            cual debe ser menor que 6"""

            favorito= int (input("Seleccione opción favorita\n"))

            if favorito < 6:
                if adivinanzas():
                    return menu(favorito - 1)
                else:
                    return True
            else:
                print("Error")
                return False
        elif opc< 6:
            print("Usted ha elegido la opción " + str(opc))
            if opc == 3:
                return False
            return True
    else:
        """en este punto vamos a validar los intentos de ingreso de opciones fallidas."""
        intentos = intentos + 1
        if intentos <= 4:
            print("Error")
            # print("Ha hecho: "+str(intentos), " intentos")
            main()
        else:
            print("Error")
            return False

"""
2 - Esta funcion muestra la lista y la ordena, según el interes del usuario,
por defecto le pasamos el valor 0 para que ordene el menú como si la primer opción 
es la favorita
"""

def menu(opc=0):

    menu = ["1. Cambiar contraseña", "2. Ingresar coordenadas actuales", "3. Ubicar zona wifi más cercana",
            "4. Guardar archivo con ubicación cercana", "5. Actualizar registros de zonas wifi desde archivo",
            "6. Elegir opción de menú favorita","7. Cerrar sesión"
            ]
    # print("tu opcion favorita fue: ", menu[opc])

    # tomamos el valor de la opcion del usuario
    favorito= str(menu[opc])

    #quitamos el item de la lista que el usuario definio para
    # no generar duplicados

    menu.pop(opc)
    # insertamos el valor en la posicion 0 del valor que tenia la opcion
    # que el usuario definio
    menu.insert(0, favorito)

    # imprimimos el muevo menu

    for item in menu:
        print(str(item), sep="\n")
    # retornamos un valor verdadero para que el usuario siga modificando el menu
    return True

"""
esta funcion es la encargada de recibir las validaciones para la ejecucion
o terminación del programa
"""
def main():
    cond= True # esta es la condicion bandera
    while cond:
        """Llamamos a la funcion validacion para verificar si los datos ingresados
        esta dentro de las opciones"""

        cond= menuInicial()

menu()
main()

"""
Referencias a variables globales

https://www.w3schools.com/python/gloss_python_global_variables.asp

"""