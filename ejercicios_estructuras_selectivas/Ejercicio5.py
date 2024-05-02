#En las líneas 1 y 2 se pregunta la edad y el género para saber que estructura utilizar
edad=int(input("¿Qué edad tienes? "))
genero=(input("¿Cuál es tu género de nacimiento? (femenino-masculino) "))
#En las líneas de la 5 hasta la 10 con la estructura IF y ELIF se hace el proceso y la operación para saber cuantas pulsaciones tiene por los 10 seg de ejercicios dependiendo de la edad y el género y luego se imprime la respuesta dependiendo de su género (femenino o masculino)
if genero=="femenino":
    numPulsaciones=(220-edad)/10
    print("El número de pulsaciones que tienes por cada 10 segundos de ejercicio aeróbico es:",numPulsaciones)
elif genero=="masculino":
    numPulsaciones=(210-edad)/10
    print("El número de pulsaciones que tienes por cada 10 segundos de ejercicio aeróbico es:",numPulsaciones)