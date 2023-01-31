""""
Reto 1

Este es programa se encarga de validar un usuario por medio del ingreso
de un usuario y contraseña prestablecidos:
usuario= 51671
clave= 17615

luego se encarga de hacer otro proceso de
verificacion por medio de un Captcha.
.....

By: Julian Dario Bejarano Gomez
Id: 000468882
código del curso: 51671

"""

import os # importamos la libreria del sistema
import time

#definimos las varables por defecto para el ingreso de los usuarios
usuario= "51671"
clave= "17615"


#esta funcion se encarga de validar los datos de ingreso
def validacion ():
    user = str(input("Ingrese el usuario: \n"))
    if user == usuario:
        pasw = str(input("Ingrese la contraseña: \n"))
        if pasw == clave:
            return True
    return False

def genCaptcha():
    # Tomamos los tres ultimos valores de la variable usuario (51671 la cual es la misma
    # del códifgo del grupo) y luego  los convertimos a numero entero

    dato1 = int(usuario [-3::])
    # Tomamos el penultimo numero del dato de usuario
    dato2 = int(usuario[-2])

    # realizamos 3 operaciones para conseguir el mismo valor del penultimo numero del usuario

    opera1= 5+1+1
    opera2= (1+1)*5-6//(1+1)
    opera3= 6*5//(6+5)-6%5+6

    # verificamos que efectivamente el penúltimo dato del usuario corresponde al resultado de las operaciones
    if opera1 == dato2 and opera2 == dato2 and opera3 == dato2:
        #enviamos el mensaje de captcha al ususario
        resultado = int(input("Ingrese el resultdo de sumar "+ str(dato1)+ " + "+ str(dato2)+ ":\n"))

        # verificamos que el resultado ingresado por el usuario es el mismo de la operacion.
        if resultado == (dato1+dato2):
            return True
        else:
            return False
def main():
    # Lo primero que aremos es limpiar la termina una vez se llama la funcion
    os.system("cls")

    print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
    print("...........................................................")

    # esperamos 1.5 segundos antes de enviar los datos de autenticacion
    time.sleep(1.5)
    if validacion ():
        print ("Captcha")
        if genCaptcha():
            print("Sesión iniciada")
            # os.system("pause")
        else:
            print("Error")
    else :
        print ("Error")

main()