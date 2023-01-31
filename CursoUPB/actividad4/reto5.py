import os
import math
import numpy as np
"""
RETO 5
By: Julian Dario Bejarano Gomez
Id: 000468882
código del curso: 51671

"""

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
ordenada = []
posActual=[]

# en este diccionario iremos adicionando los datos que luego se exportarán como archivo
informacion= {
        'actual':[],
        'zonawifi1':[],
        'recorrido':[]
    }

Sup = 1.998
Inf = 1.740
Or = -75.689
Occ = -75.950
r= 6372.795477598
count=1

"""Seccion del reto 5"""
def leerArchivo():
    try:
        with open('tabla.txt','r',encoding="utf-8") as fh:
            # especificamos que vamos a leer una por una las lineas del archivo
            data = fh.readlines()
            # llamamos una funcion que borra los datos de la tabla inicial,
            # para luego cargarles los datos que están en el archivo .txt
            borrarTabla(tabla)

            for line in data:
                # si leemos directamente el archivo, nos va a cargar los saltos de linea (\n) como caracter,
                # por esa razon usamos el metodo strip(), para eliminar los espacios y saltos de linea
                # unavez esta sin estos caracteres,
                # usamos el método split para especificar que la coma(,) es el caracter que divide cada dato,
                # este metodo ademas permite que los saltos de linea en el archivo sean interpretados como
                # una nueva row (fila)
                # Ref:
                # https://stackoverflow.com/questions/53000522/how-to-read-text-file-into-matrix-in-python

                split_line= line.strip().split(",")

                # ahora convertimos cada dato del archivo en un flotante, de lo contrario lo interpretara como una cadena de
                # caracteres

                flotantes= [float(x) for x in split_line]
                # en este punto adicionamos a la tabla de posiciones los datos almacenados en el archivo
                tabla.append(flotantes)
        print("Datos cargados:", tabla)
        opc = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal\n"))
        if opc == 0:
            # print(tabla)
            menu()
            return True
        else:
            return False
    except:
        return EnvironmentError

def borrarTabla(tab):

    # siqueremos saber el numero de filas o columnas de un archivo
    numRow= len(tab)
    # numCol= len(tab[0])
    # print (numRow,numCol)

    # en el siguiente método tomamos el numero de filas y borramos la fila 0
    # esa misma cantidad de veces, esto garantiza que borraremos la totalidad de las filas de
    # una tabla.
    # Ref:
    # https://www.tutorialgateway.org/python-list-del-function/

    for row in range(0,numRow):
        del tab[0]

    # tabla =np.array(tabla)
    # en numpy si decimos axis=0 nos referimos a que las operaciones las haremos en las filas
    # mientras que axis=1, indica que las operaciones las haremos en las columnas.
    # tabla =np.delete(tabla, (numRow-1), axis= 0)
    # print("borrado:",tabla)


def diccionarioToArchivo():
    """referencias para exportar archivos:
    https://pythonspot.com/save-a-dictionary-to-a-file/
    """
    try:
        print(informacion)
        opc= int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal\n"))
        if opc== 0 or opc ==1:
            if opc == 1:
                archivo=open("datos.txt","w")
                print("Exportando archivo")
                # de esta manera exportamos el diccionario como un texto.
                archivo.write(str(informacion))
                # for key,value in informacion.items:
                #     archivo.write(key,value)
                #     archivo.close()
                # menu()
                return False
            else:
                return True

    except:
        return ValueError

"""
Seccion del Reto 4
"""
def comparar(lat,lon):
    # recorremos la tabla que contine los datos de cordenadas y usuarios
    for dato in tabla:
        global count
        # adquirimos los datos de lat y lon de  esa tabla
        latTabla=dato[0]
        lonTabla=dato[1]

        # enviamos a la funcion distancia los datos de la posicion actual del usuario
        # y las posiciones de la tabla, para que evalue las distancias
        dis= round(distancia(lat,latTabla,lon,lonTabla))
        # print("La zona wifi",count,": ubicada en",dato,"a",dis,"metros, tiene en promedio",dato[2],"usuarios")

        # adicionamos a las listas los datos de las distancias y los usuarios
        distancias.append(dis)
        numUsuarios.append(dato[2])
        count = count + 1
    count=1
    # x = np.array(distancias)
    # print("numpy",x)


    """una vez tenemos las listas, vamos a crear una lista con los indices
    que muestran en que posiciones están los valores desde el menor valor al mayor valor, es importante notar que ordenamos 
    los valores de una lista segun su valor y con respecto a los valores de otra lista, esto quiere decir, que si bien
    ordenamos la lista 1 en relacion con sus valores, tambien lo hacemos en relacion a los valores de la segunda lista (lo que vendria a hacer su pareja)
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

    # ahora comparamos si el numero de usuarios entre los dos lugares mas cercanos e imprimimos de primeras el
    # lugar que tenga menos usuarios... (si los usuarios del sitio 1 son menores que el sitio 2.... )

    if ordenada[0][3]<= ordenada[1][3]:
        for i in range(0,2):
            print("La zona wifi", step, ": ubicada en", ordenada[i][0:2], "a", ordenada[i][2], "metros, tiene en promedio", ordenada[i][3], "usuarios")
            step= step+1
        opc= int(input("Elija 1 0 2 para recibir indicaciones de llegada: \n"))
        opc= opc-1

    # en caso de que el segundo sitio mas cercano tenga menores usuarios lo imprimimos de primeras,
    # por lo tanto recorremos el arreglo desde la posicion 1 a la 0
    else:
        # ciclo de 1 a 0(-1) decreciendo -1
        for i in range(1,-1,-1):

            print("La zona wifi", step, ": ubicada en", ordenada[i][0:2], "a", ordenada[i][2], "metros, tiene en promedio", ordenada[i][3], "usuarios")
            step= step+1
        opc= int(input("Elija 1 0 2 para recibir indicaciones de llegada: \n"))

        #
        # en este caso debemos convertir la opcion que ingreso el usuario en el indice del dato que realmente eligio, es decir, como mostramos el arreglo al reves
        # el usuario al elegir la opcion 1, en verdad hace referencia a la posicion 2 del arreglo, y al elegir la opcion 2 en verdad hace referencia a la
        # posicion 1 del arreglo, por lo tanto convertimos la variable opcion al indice, de la siguiente forma:

        opc= abs(opc-3)
    step = 0
    if opc== 1 or opc== 0:
        # enviamos los daos de las elecciones a las funciones que se encargan de mostrar el recorrido y los tiempos de llegada.
        recorrido(lat,lon, ordenada[opc][0], ordenada[opc][1],ordenada[opc][3])
        tiempoRecorrido(ordenada[opc][2])
        if int(input("Presione 0 para salir\n")) == 0:
            os.system("cls")
            # borramos las tablas por si los datos de la ubicación de los puntos cercanos cambian (opcion 5 del menu)
            borrarTabla(ordenada)
            borrarTabla(distancias)
            borrarTabla(numUsuarios)
            menu()
            return True
        else:
            print("Error zona wifi")
            return False
    else:
        print("Error zona wifi")
        return False


# con esta función determinamos las distancias entre dos puntos,
# conociendo la latitud y la longitud  de ambos puntos

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

# en estafunción comparamos la latitud inicial con la latitud de destino,
# la long inicial con la long de destino para saber que orientación debe
# tomar el usuario, además, en esta función adicionamos datos al diccionario que
# luego se exportará como archivo

def recorrido(latIni,lonIni, latDes, lonDes, usuarios):
    # print(latIni,lonIni, latDes, lonDes)
    if latDes>latIni:
        vert = "norte"
    else:
        vert = "sur"
    if lonDes> lonIni:
        hori= "Occidente"
    else:
        hori= "oriente"

    #     agregamos al diccionario la informacion de las latitudes actuales, las de la zona wifi elegida
    informacion['actual']=[latIni, lonIni]
    informacion['zonawifi1']=[latDes,lonDes,usuarios]


    print("Para llegar a la zona wifi debe dirigirse primero al",hori,"y luego hacia el",vert)


def tiempoRecorrido(distancia):
    tiempoBus= distancia/16.67
    tiempoCami=distancia/0.483
    print("El tiempo en bus es:", round(tiempoBus),"minutos")
    print("El tiempo caminando es:", round(tiempoCami),"minutos")

    informacion['recorrido']=[distancia,"bus",round(tiempoBus)]
"""
RETO 3



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
    if opc== 2022:
        lat= float(input("ingrese su latitud:\n"))
        if lat<0:
            print("El huso horario es -5")
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
                    posActual.append([float(coordenadas[opc-1][0]),float(coordenadas[opc-1][1])])
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

        elif opc == 4:
            if len(coordenadas) > 1 and len(posActual)>0:
                if diccionarioToArchivo():
                    return True
            else:
                print("Error de alistamiento")
                return False
        elif opc==5:
            if leerArchivo():
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
    # os.system("pause")
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

def promedio(num):
    numeros=[]
    for i in range(0,num):
        dato= float(input("ingrese dato"+ str(i+1)))
        numeros.append(dato)
    suma= sum(numeros)
    prom=suma/len(numeros)
    print("el promedio es:",prom)

#esta funcion se encarga de validar los datos de ingreso corresponden al reto1
def validacion ():
    user = str(input("Ingrese el usuario: \n"))
    if user == "Tripulante2022":
        print("Este fue mi primer programa y vamos por más")
        return False
    elif user == usuario:
        pasw = str(input("Ingrese la contraseña: \n"))
        if pasw == "m1s10nt1c":
            opc=int(input("cuantos datos desea ingresar:\n"))
            promedio(opc)

        elif pasw == clave:
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


# impCoordenadas(coordenadas)
# comparar(1.963, -75.712)
# print(distancias)
# 2.3943223575350774,-71.53935013473802 2.054003264372146,-70.53076117284843
# distancia(2.3943223575350774,2.054003264372146,-71.53935013473802,-70.53076117284843)
# crearDiccionario()
# print(informacion)
# informacion['actual'][1]= "cian"
# print(informacion)

if saludo():
    menu()
    main()
#
# menu()
# main()


"""
Referencias a variables globales

https://www.w3schools.com/python/gloss_python_global_variables.asp

"""