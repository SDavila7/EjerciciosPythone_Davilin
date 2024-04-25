nameStudent=(input("Digita tu nombre:")) #Se pregunta acerca del nombre del estudiante
actEnClase=float(input("Digite la calificación promedio de las actividades realizadas en clase:")) #Se pide digitar la calificación promedio de las actividades que se realizaron en la clase
proyectoFinal=float(input("Digite la calificación del proyecto final:")) #Se pide digitar la calificación del proyecto final del estudiante
evaluacionesParciales=float(input("Digite la calificación promedio de las evaluaciones o parciales:")) #Se pide digitar la calificación promediada acerca de las evaluaciones o parciales
notaActividades = actEnClase * 0.3 #Se realiza la operación de la calificación promedio de las actividades en clase por el porcentaje que tiene en la nota final (30%)
notaProyecto = proyectoFinal * 0.5 #Se realiza la operación de la calificación del proyecto final por el porcentaje que tiene en la nota final (50%)
notaParciales = evaluacionesParciales * 0.2 #Se realiza la operación de la calificación del promedio de las evaluaciones por el porcentaje que tiene en la nota final (20%)
notaFinal=notaActividades+notaParciales+notaProyecto #Se hace la suma entre la nota porcentada de las actividades en clase, más la nota porcentada del proyecto final y la nota porcentada de las evaluaciones
print("La nota final de algoritmia del estudiante",nameStudent,"es:",notaFinal) #Se muestra el mensaje del nombre del estudiante y la nota final de la materia de algoritmia