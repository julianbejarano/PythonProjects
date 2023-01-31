"""
Este programa se encarga de hayar la pendidente de una recta
teniendo dos puntos y siempre y cuando X sea siempore mayor que 0
(es decir que la recta no corte el eje y)
para el ejemplo utilizaremos los puntos (3,5)(6,12)

By: Julian Dario Bejarano Gomez
Id: 000468882
código del curso: 51671
"""

x1= 3
x2= 6
y1= 5
y2= 12

pendiente= (y2-y1)/(x2-x1)

print ("La pendiente que pasa por el punto: ("+str(x1)+", "+str(y1)+") y el punto: ("+str(x2)+", "+str(y2)+") es:\n "+ str (pendiente))
b= y1- (pendiente*x1)
print("Y la ecuacion de la recta es:\n Y= "+str (pendiente)+" X + ("+ str(b)+")")