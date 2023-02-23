# = Tiempo promedio por vuelta

# = Solicitamos el tiempo de cada vuelta al usuario
vuelta1 =  float(input("Cual es el tiempo de la primera vuelta: "))

vuelta2 =  float(input("Cual es el tiempo de la segunda vuelta: "))

vuelta3 =  float(input("Cual es el tiempo de la tercera vuelta: "))

vuelta4 =  float(input("Cual es el tiempo de la cuarta vuelta: "))

vuelta5 =  float(input("Cual es el tiempo de la quinta vuelta: "))

# = Sumamamos cada tiempo y se divide entre 5 para sacar el promedio de cada vuelta
vueltas = (vuelta1 + vuelta2 + vuelta3 + vuelta4 + vuelta5)  / 5

# = Imprimimos el resultado
print("El promedio por vuelta es de: " + str(vueltas) + " segundos")

# = Tiempo promedio de los pits

# = Solicitamos al usuario el tiempo en cada parada de lo pits 
pits1 =  float(input("Cual es el tiempo en la primera parada en los pits: "))

pits2 =  float(input("Cual es el tiempo de la segunda parada en los pits: "))

pits3 =  float(input("Cual es el tiempo de la tercera parada en los pits: "))

pits4 =  float(input("Cual es el tiempo de la cuarta parada en los pits: "))

pits5 =  float(input("Cual es el tiempo de la quinta parada en los pits: "))

# = Sumamos cada tiempo y se divide entre 5 para sacara el promedio de cada vuelta

pits = (pits1 + pits2 + pits3 + pits4 + pits5) / 5
# = Imprimimos el resultado
print("El promedio de tiempo en los pits es de: " + str(pits) + " segundos")


# = Porcentaje del tiempo en los pits recorrido en una vuelta

# = Calculamos el porcentaje 
porcentaje = pits * 100 / vueltas

# = Imprimimos el resultado 
print("El porcentaje del tiempo en pits en una vuelta es de: " +str(porcentaje) + "%")