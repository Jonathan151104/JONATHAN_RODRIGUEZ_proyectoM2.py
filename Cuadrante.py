#Hola
#Aquí le pedimos al usuario que ingrese las coordenadas de (x) y (y), a la cual se guardan en las variables del mismo nombre caracter.
#Ambas son del mismo tipo de dato entero.
x = int(input("¡Hola! Ingresa el valor, de la primer coordenada en x: "))
y = int(input("Ingresa el valor, de la segunda coordenada en y: "))

#La condicón muestra si el eje (x) y el eje (y), son iguales a cero, muestre el siguiente mensaje.
if x == 0 and y == 0 :
    print("Inicie de nuevo, los cuadrantes tienen que ser mayor a 0")

#Si no que el eje (x), sea igual a 0 y el eje (y), tiene un valor. Muestra el siguiente mensaje.
elif x == 0 :
    print("El (eje x) nesecita un valor mayor que 0")

#Ahora bien el eje (y), sea igual a 0 y el eje (x), tiene un valor. Muestra el siguiente mensaje.
elif y == 0: 
    print("El (eje y) nesecita un valor mayor que 0")

#Aquí decide si el eje (x) y el eje (y), tiene un valor mayor a 0, muestra el siguiente mensaje.
elif x > 0 and y > 0 :
    print("El punto se encuentra en el Cuadrante I")

#Si no, entonces el eje (x), es menor a 0 y el eje (y), mayor que 0 define el siguiente mensaje.
elif x < 0 and y > 0 :
    print("El punto se encuentra en el Cuadrante II")

#Si tampoco fue, ahora el escenario cambia, ahora el eje (x) y el eje (y), son menores a 0 muestra otro mensaje.
elif x < 0 and y < 0 :
    print("El punto se encuentra en el Cuadrante III")

#De lo contrario, si el eje (x), tiene un valor mayor a 0 y el eje (y), un valor menor a 0 muestra otro mensaje.
elif x > 0 and y < 0 :
    print("El punto se encuentra en el Cuadrante IV")