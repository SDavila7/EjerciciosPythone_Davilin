#En las lineas 2 y 3 se declaran las variables de las edades según lo que corresponda (meses o años)
edadMeses=0
edadAños=0
#Las líneas de la 5 hasta la línea 9 se utiliza la estructura IF y ELIF para saber si es mayor a 12 meses o menor
mayor12=(input("¿Eres mayor a 12 meses? (minúsculas por favor): "))
if mayor12=="si":
    edadAños=int(input("Puedes digitar cuántos años tienes por favor: "))
elif mayor12=="no":
    edadMeses=int(input("Puedes digitar cuántos meses tienes por favor: "))
#En las líneas 11 y 12 se pregunta por el nivel de hemoglobina y si su género es masculino o femenino 
nivelHemoglobina=float(input("Por favor puedes introducir tu nivel de hemoglobina en g%: "))
genero=input("Por favor puedes introducir tu género de nacimiento por favor (femenino-masculino): ")
#En las líneas de la 14 hasta la 36 se utilizan las distintas estructuras de IF,ELIF,ELSE para hacer el proceso de determinar según la hemoglogina ingresada, su edad y su género si tiene o no anemia
if edadMeses<=1:
    rango = (13, 26)
elif edadMeses>=2 and edadMeses<=6:
    rango = (10, 18)
elif edadMeses>=7 and edadMeses<=12:
    rango = (11, 15)
elif edadAños>=2 and edadAños<=5:
    rango = (11.5, 15)
elif edadAños>=6 and edadAños<=10:
    rango = (12.6, 15.5)
elif edadAños>=11 and edadAños<=15:
    rango = (13, 15.5)
elif genero.lower() == 'femenino':
    rango = (12, 16)
elif genero.lower() == 'masculino':
    rango = (14, 18)
else:
    print ("Por favor introduce un género válido: 'femenino' o 'masculino'.")

if nivelHemoglobina < rango[0]:
    print ("Eres positivo para anemia")
else:
    print ("Eres negativo para anemia")