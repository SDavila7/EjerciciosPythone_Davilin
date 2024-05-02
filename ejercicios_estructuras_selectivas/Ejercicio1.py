#De la línea 2 hasta la línea 4 se preguntan las notas que tiene el estudiante en algoritmia
nota1=float(input("Digita la primer nota de algoritmia: "))
nota2=float(input("Digita la segunda nota de algoritmia: "))
nota3=float(input("Digita la tercer nota de algoritmia: "))
#Las líneas 6 y 7 se hace la operación de sumar las tres notas y dividirlas por la cantidad de notas que hay y, así mostrar si aprobó o no la materia de algoritmia
notaDefinitiva=(nota1+nota2+nota3)/3
print("Has aprobado algoritmia" if notaDefinitiva>= 70 else "No has aprobado algoritmia")