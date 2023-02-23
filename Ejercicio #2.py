# = Imprimimos el menu

print("Menu principal")
print("Elija una opcion")
print("1..Camisa")
print("2..Pantalon")
print("3..Sueter")
print("4..Falda")
print("5..Blusa")
print("0..Salir")

opcion = -1
# = Interaccion del usuario
while opcion != 0:
    opcion = int(input("Opcion: ")) # = Solicitamos al usuario la opcion
    if opcion == 0:
        print("Muchas gracias, vuelva pronto") # = Si responde con 0 imprimimos una despedida
        
    elif opcion == 1: # = Si el usuario responde con 1
        print("El precio de la camisa es de 5$") # = Imprimimos el precio de articulo
        cantidad1 = int(input("Cantidad que desea comprar: ")) # = Solicitamos la cantidad que desea llevar 
        cantidadTotal1 = cantidad1 * 5 # = Se hace la operacion de cantidad por el precio 
        print("El monto a pagar es de: " +str(cantidadTotal1) + "$") # = Imprimimos el resultado
        

    elif opcion == 2: # = Si el usuario responde con 2
        print("El precio de pantalon es de 10$") # = Imprimimos el precio de articulo
        cantidad2 = int(input("Cantidad que desea comprar: ")) # = Solicitamos la cantidad que desea llevar 
        cantidadTotal2 = cantidad2 * 10 # = Se hace la operacion de cantidad por el precio 
        print("El monto a pagar es de: " +str(cantidadTotal2) + "$") # = Imprimimos el resultado
        

    elif opcion == 3: # = Si el usuario responde con 3
        print("El precio del sueter es de 15$") # = Imprimimos el precio de articulo
        cantidad3 = int(input("Cantidad que desea comprar: ")) # = Solicitamos la cantidad que desea llevar 
        cantidadTotal3 = cantidad3 * 15 # = Se hace la operacion de cantidad por el precio 
        print("El monto a pagar es de: " +str(cantidadTotal3) + "$") # = Imprimimos el resultado
        

    elif opcion == 4: # = Si el usuario responde con 4
        print("El precio de la falda es de 5$") # = Imprimimos el precio de articulo
        cantidad4 = int(input("Cantidad que desea comprar: ")) # = Solicitamos la cantidad que desea llevar 
        cantidadTotal4 = cantidad4 * 5 # = Se hace la operacion de cantidad por el precio 
        print("El monto a pagar es de: " +str(cantidadTotal4) + "$") # = Imprimimos el resultado
        

    elif opcion == 5: # = Si el usuario responde con 5
        print("El precio de la blusa es de 5$") # = Imprimimos el precio de articulo
        cantidad5 = int(input("Cantidad que desea comprar: ")) # = Solicitamos la cantidad que desea llevar 
        cantidadTotal5 = cantidad5 * 5 # = Se hace la operacion de cantidad por el precio 
        print("El monto a pagar es de: " +str(cantidadTotal5) + "$") # = Imprimimos el resultado
        