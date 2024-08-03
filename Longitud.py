#Solo prueba
#Aquí le estemos pedimos una palabra al usuario y se aguarda en la variable (frase) de tipo de string.
frase = input("Ingresa una palabra, por favor: ")

#Ahora si la longitud de la palabra que se alla puesto en la variable (frase), es mayor o igual a 4 y menor o igual a 8.
#Muestra el siguiente mensaje
if len(frase) >= 4 and len(frase) <= 8 :
    print("La palabra es correcta")

#Si no fue lo anteror si la longitud de la palabra almacenada en (frase), es menor a 4, muestra otro mensaje.
elif len(frase) < 4 :
    n = 4 - len(frase) 
    r = 4 + n
    print("Hacen falta letras. Solo tiene ",  len(frase), " letra(s), te faltan "+ str (n) +" a " + str(r) +" letras.")

#De lo contrario se hace una resta de longitud o el número de letras de la palabra (frase), menos 8.
#Se almacena en la variable (t) y muestra el siguiente mensaje.
else :
    t = len(frase) - 8
    print("Sobran letras. Tiene ", len(frase), " letras , necesitas quitar "+ str(t) +" letra(s), tienen que ser de 4 a 8 letras.")