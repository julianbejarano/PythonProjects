import os
import math
import numpy as np
import time


#definimos las varables por defecto para el ingreso de los usuarios
usuario= "51671"
clave= "17615"
contrasena=["123456"] #definimos el campo que guardará la contraseña
coordenadas=[]
# coordenadas=[['1.963', '-75.712'], ['1.964', '-75.713'], ['1.965', '-75.714']]
# lat,lon,usu
tabla=[[1.811,-75.820,58],[1.919,-75.843,1290],[1.875,-75.877,110],[1.938,-75.764,114]]

# esta matriz nos permite guardar las distancia comparadas
distancias=[]
numUsuarios=[]

Sup = 1.998
Inf = 1.740
Or = -75.689
Occ = -75.950
r= 6372.795477598
count=1
"""
Seccion del Reto 4
"""
def comparar(lat,lon):
    # recorremos la tabla que contine los datos de cordenadas y usuarios
    ordenada=[]
    for dato in tabla:
        global count
        # adquirimos los datos de lat y lon de  esa tabla
        latTabla=dato[0]
        lonTabla=dato[1]
        # enviamos a la funcion distancia esos datos
        dis= round(distancia(lat,latTabla,lon,lonTabla))
        # print("La zona wifi",count,": ubicada en",dato,"a",dis,"metros, tiene en promedio",dato[2],"usuarios")

        # adicionamos a las listas los datos de las distancias y los usuarios
        distancias.append(dis)
        numUsuarios.append(dato[2])
        count = count + 1
    # x = np.array(distancias)
    # print("numpy",x)


    """una vez tenemos las listas, vamos a crear una lista con los indices
    que muestran en que posiciones están los valores desde el menor valor al mayor valor, es importante notar que ordenamos 
    los valores de una lista segun su valor y con respecto a los valores de otra lista
    """

    ind = np.lexsort((numUsuarios, distancias))  # Sort by a, then by b

    # print(ind)
    # print("distancias y usuarios:")
    #
    # # como ind guarda las posiciones donde estan los datos menores, imprimimos dicha posicion
    # # tanto de la lista distancias como en la lista numUsuarios
    #
    # [print((distancias[i], numUsuarios[i])) for i in ind]

    # creamos una matriz ordenada con los datos Lat, Lon, dista y usuarios

    [ordenada.append([tabla[i][0],tabla[i][1],distancias[i], numUsuarios[i]]) for i in ind]
    step = 1
    if ordenada[0][3]<= ordenada[1][3]:
        for i in range(0,2):
            print("La zona wifi", step, ": ubicada en", ordenada[i][0:2], "a", ordenada[i][2], "metros, tiene en promedio", ordenada[i][3], "usuarios")
            step= step+1
        opc= int(input("Elija 1 0 2 para recibir indicaciones de llegada: \n"))
        opc= opc-1

    else:
        # ciclo de 1 a 0(-1) decreciendo -1
        for i in range(1,-1,-1):

            print("La zona wifi", step, ": ubicada en", ordenada[i][0:2], "a", ordenada[i][2], "metros, tiene en promedio", ordenada[i][3], "usuarios")
            step= step+1
        opc= int(input("Elija 1 0 2 para recibir indicaciones de llegada: \n"))
        opc= abs(opc-3)
    if opc== 1 or opc== 0:
        recorrido(lat,lon, ordenada[opc][0], ordenada[opc][1])
        tiempoRecorrido(ordenada[opc][2])
        if int(input("Presione 0 para salir\n")) == 0:
            os.system("cls")
            menu()
            return True
        else:
            print("Error zona wifi")
            return False
    else:
        print("Error zona wifi")
        return False




def distancia(lat1, lat2,lon1,lon2):
    # para este ejercicio se ha utilizado una fórmula dada por la guia
    # es conveniente revisar la documentación de la formula
    # https://www.ehowenespanol.com/calcular-distancia-puntos-latitud-longitud-como_452715/

    difLat= lat2-lat1
    # print(difLat)
    diflon= lon2-lon1
    # print(diflon/2)
    prod= (math.sin(difLat/2))**2+math.cos(lat1)*math.cos(lat2)*(math.sin(diflon/2))**2
    # print(prod)
    try:
        dis= 2*r*(math.asin(math.sqrt(prod)))
        # print("la distancia es: ",dis)
        return dis
    except:
        return ValueError

def recorrido(latIni,lonIni, latDes, lonDes):
    # print(latIni,lonIni, latDes, lonDes)
    if latDes>latIni:
        vert = "norte"
    else:
        vert = "sur"
    if lonDes> lonIni:
        hori= "Occidente"
    else:
        hori= "oriente"

    print("Para llegar a la zona wifi debe dirigirse primero al",hori,"y luego hacia el",vert)


def tiempoRecorrido(distancia):
    tiempoBus= distancia/16.67
    tiempoCami=distancia/0.483
    print("El tiempo en bus es:", round(tiempoBus),"minutos")
    print("El tiempo caminando es:", round(tiempoCami),"minutos")
"""
RETO 3

By: Julian Dario Bejarano Gomez
Id: 000468882
código del curso: 51671

Seccion del RETO 2.
Este programa se encarga de la ordenacion de una lista segun el interes del usuario,
es imPortante aclarar que la lista se ordena cada vez que el usuario accede a su midificacion,
por lo tanto, la lista toma un orden básico y luego lo modifica segun la opcion ingresada,
si el usuario se equivoca 3 veces consecutivas en la eleccion del menú inicial, el programa
envia el mensaje error y se termina su ejecución.

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

    opc = input("Elija una opción:\n")
    # print("Haz elegido la opción: ", str(opc))

    opc= int(opc)
    if opc== -1:
        print("Usted está en hemisferio sur")
        return False
    if opc <8 and opc> 0:

        if opc == 1:
            if cambioPass(contrasena):
                return True

        elif opc == 2:
            if modCoordenada(coordenadas):
                return True
        elif opc == 3:
            if len(coordenadas)>1:
                impCoordenadas(coordenadas)
                opc= int(input("Por favor elija su ubicación actual(1,2 ó 3) para calcular la distancia a los puntos de conexión\n"))
                # enviamos a la funcion de distancias y tiempos el dato de la coordenada favorita
                if opc>=1 and opc<=3:
                    if comparar(float(coordenadas[opc-1][0]),float(coordenadas[opc-1][1])):
                        return True
                    else:
                        return False
                else:
                    print("Error ubicación")
                    return False
            else:
                print("Error sin registro de coordenadas")
                return False
            menu()
            return True
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
        elif opc == 7:
            print("Hasta pronto")
            os.system("pause")
            return False

        else:
            print("Usted ha elegido la opción " + str(opc))
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



"""
seccion del reto 3
Para las siguientes opciones observaremos que se pasan por parámetros listas y matrices.
esto permite la modificacion de los valores al interior de las funciones, básicamente
es lo mismo que pasa con las variables globales, pero este es un método un poco mas limpio.
Algo a tener en cuenta que al modificar las listas y matrices o diccionarios (objetos) en alguna función
que lo haya aceptado como parámetro, se modifica el valor guardado en memoria de estos objetos. 
"""

def cambioPass(contrasena):
    validacion= input("Ingrese contraseña anterior: ")
    if validacion == contrasena[0]:
        nueva= input("Ingrese su nueva contraseña: ")

        if nueva == contrasena[0]:
            print("Error")
            return False
        else:
            contrasena[0]= nueva
            print("Contraseña modificada")
            os.system("cls")
            os.system("pause")
            menu()
            return True
    else:
        print("Error")
        return False

def valLatitud():
    latitud = str(input("Latitud: "))

    if len(latitud)>=0 and "." in latitud:
        partes = latitud.split(".")  # dividimos la cadena por el punto
        if len(partes[1]) == 3:

            # validaremos que esté en el rango, para ello debemos convertir el string en float
            if float(latitud) < Inf or float(latitud) > Sup:
                print("Error coordenada")
                return False
            else:
                return latitud
        else:
            print("el dato no contiene 3 decimales")
            return False
    else:
        print("Error coordenada")
        return False

def valLongitud():
    longitud = str(input("Longitud: "))
    if len(longitud)>=0 and "." in longitud:
        partes = longitud.split(".")  # dividimos la cadena por el punto
        if len(partes[1]) == 3:

            # validaremos que esté en el rango, para ello debemos convertir el string en float
            if float(longitud) < Occ or float(longitud) > Or:
                print("Error coordenada")
                return False
            else:
                return longitud
        else:
            print("el dato no contiene 3 decimales")
            return False
    else:
        print("Error coordenada")
        return False

def ingresarCoordenadas(coordenadas):
    for i in range(3):
        print("Ingrese el dato ", i+1)
        lat = valLatitud()
        if lat:
            lon = valLongitud()
            if lon:
                print(lat, lon)
                coordenadas.append([lat, lon])
                print("Dato ", i+1, " ingresado con éxito.")
            else:
                # print("error")
                return False

        else:
            # print("error")
            return False
    os.system("cls")
    os.system("pause")
    menu()
    return True

def impCoordenadas(coordenadas):
    for i in range(0,len(coordenadas)):
        print("Coordenada [latitud,longiud]", i+1, ":", coordenadas[i])

def modCoordenada(coordenadas):
    if len(coordenadas)>0:
        impCoordenadas(coordenadas)
        minMaxLat(coordenadas)
        minMaxLon(coordenadas)

        pos = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. "
                        "Presione 0 para regresar al menú\n"))
        pos = pos-1
        if pos== -1:
            # print("regreso al menu principal")
            menu()
            return True
        elif pos in range(0,len(coordenadas)):
            print("Ingrese nuevas coordenadas:")
            lat = valLatitud()
            if lat:
                lon = valLongitud()
                if lon:
                    print(lat, lon)
                    coordenadas[pos]=[lat, lon]
                    print("Coordenada cambiada exitosamente")
                    menu()
                    return True

        else:
            print("Error actualización")
    #         ir al menu
    else:
        print("Aun no hay datos en las coordenadas")
        if ingresarCoordenadas(coordenadas):
            return True

def minMaxLat(coordenadas):
    # Con el siguiente metodo creamos una lista con los valores [0] de la matriz de entrada
    lat= [x[0] for x in coordenadas]
    # obtendremos la posicion del valor con mayor y menor valor
    minpos = lat.index(min(lat))
    maxpos = lat.index(max(lat))
    # print(lat)
    # print("La coordenada", minpos + 1,"es la que esta mas al sur")
    print("La coordenada", maxpos + 1,"es la que esta mas al norte")

def minMaxLon(coordenadas):
    # Con el siguiente metodo creamos una lista con los valores [1] de la matriz de entrada
    lon= [x[1] for x in coordenadas]
    # obtendremos la posicion del valor con mayor y menor valor
    minpos = lon.index(min(lon))
    maxpos = lon.index(max(lon))
    # print(lon)
    print("La coordenada", minpos + 1,"es la que esta mas al oriente")
    # print("La coordenada", maxpos + 1, "es la que esta mas al occidente")
impCoordenadas(coordenadas)
# comparar(1.963, -75.712)
# print(distancias)
# 2.3943223575350774,-71.53935013473802 2.054003264372146,-70.53076117284843
# distancia(2.3943223575350774,2.054003264372146,-71.53935013473802,-70.53076117284843)




#esta funcion se encarga de validar los datos de ingreso
def validacion ():
    user = str(input("Ingrese el usuario: \n"))
    if user == "Tripulante2022":
        print("Este fue mi primer programa y vamos por más")
        return False
    elif user == usuario:
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
def saludo():
    # Lo primero que aremos es limpiar la termina una vez se llama la funcion
    os.system("cls")

    print("\nBienvenido al sistema de ubicación para zonas públicas WIFI")
    print("...........................................................")

    # esperamos 1.5 segundos antes de enviar los datos de autenticacion
    # time.sleep(1.5)
    if validacion ():
        print ("Captcha")
        if genCaptcha():
            print("Sesión iniciada")
            return True
        else:
            print("Error")
            return False
    else :
        # print ("Error")
        return False

if saludo():
    menu()
    main()


"""
Referencias a variables globales

https://www.w3schools.com/python/gloss_python_global_variables.asp

"""